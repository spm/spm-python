# MNE2MATLAB2MNE - reads in and preprocesses data using MNE, then moves to SPM to do specific preprocessing, then moves back to MNE for the rest of the analysis


import matplotlib.pyplot as plt
import numpy as np
import mne
from spm import Struct, spm_opm_amm
from spm.utils import spm_2_mne_raw, mne_raw_2_spm

plt.ion()

# 1. read in the data using mne
subject = "sub-002"
data_path = mne.datasets.ucl_opm_auditory.data_path()
opm_file = (
    data_path / subject / "ses-001" / "meg" / "sub-002_ses-001_task-aef_run-001_meg.bin"
)
subjects_dir = data_path / "derivatives" / "freesurfer" / "subjects"

raw = mne.io.read_raw_fil(opm_file, verbose="error")
raw.crop(120, 210).load_data()

# 2. Plot raw data using mne
picks = mne.pick_types(raw.info, meg=True)
amp_scale = 1e12  # T->pT
stop = len(raw.times) - 300
step = 300
data_ds, time_ds = raw[picks[::5], :stop]
data_ds, time_ds = data_ds[:, ::step] * amp_scale, time_ds[::step]

fig, ax = plt.subplots(layout="constrained")
plot_kwargs = dict(lw=1, alpha=0.5)
ax.plot(time_ds, data_ds.T - np.mean(data_ds, axis=1), **plot_kwargs)
plt.grid(True)
set_kwargs = dict(
    ylim=(-500, 500), xlim=time_ds[[0, -1]], xlabel="Time (s)", ylabel="Amplitude (pT)"
)
ax.set(title="No preprocessing", **set_kwargs)
plt.show()

psd_kwargs = dict(fmax=100, n_fft=int(round(raw.info["sfreq"]) * 2 * 2))
raw.compute_psd(**psd_kwargs).plot(dB=True, amplitude=True)

# 2. Some preproceesing using mne
raw.notch_filter(np.arange(50, 251, 50), notch_widths=4)
raw.filter(1, 70, picks="meg")

ref_mag_name = [
    ch["ch_name"]
    for ch in raw.info["chs"]
    if ch["kind"] == mne.io.constants.FIFF.FIFFV_REF_MEG_CH
]
raw.info["bads"] = ref_mag_name
# raw.info['bads'].extend(['G2-A4-RAD','G2-17-TAN'])


# 3. MNE 2 SPM
data = mne_raw_2_spm(raw, "D:/opm-tutorial")
data

# 4. SPM prossesing
S = Struct()
S.D = data
mD = spm_opm_amm(S)


# 5. SPM 2 MNE
cleaned_data = spm_2_mne_raw(mD)
cleaned_data


# 6. MNE plotting
psd_kwargs = dict(fmax=100, n_fft=int(round(cleaned_data.info["sfreq"]) * 2 * 2))
cleaned_data.compute_psd(**psd_kwargs).plot(dB=True, amplitude=True)


picks = mne.pick_types(cleaned_data.info, meg=True)
amp_scale = 1e12  # T->pT
stop = len(cleaned_data.times) - 300
step = 300
data_ds, time_ds = cleaned_data[picks[::5], :stop]
data_ds, time_ds = data_ds[:, ::step] * amp_scale, time_ds[::step]

fig, ax = plt.subplots(layout="constrained")
plot_kwargs = dict(lw=1, alpha=0.5)
ax.plot(time_ds, data_ds.T - np.mean(data_ds, axis=1), **plot_kwargs)
ax.grid(True)
set_kwargs = dict(
    ylim=(-500, 500), xlim=time_ds[[0, -1]], xlabel="Time (s)", ylabel="Amplitude (pT)"
)
ax.set(title="No preprocessing", **set_kwargs)
plt.show()


# 7. MNE epoching
events = []
events = mne.find_events(cleaned_data, stim_channel="NI-TRIG", min_duration=0.001)
events_dict = {"trigger": 3}

cleaned_data.filter(2, 40, picks="meg")
epochs = mne.Epochs(
    cleaned_data,
    events,
    tmin=-0.1,
    tmax=0.4,
    event_id=events_dict,
    detrend=1,
    baseline=[-0.05, 0],
    preload=True,
)


evoked = epochs["trigger"].average()
evoked.plot()


radial_channels = [
    ch for ch in evoked.ch_names if ch.endswith("RAD")
]  # take on radial sensors
evoked_radial = evoked.pick_channels(radial_channels)
fig = evoked_radial.plot_joint()


tang_channels = [
    ch for ch in evoked.ch_names if ch.endswith("TAN")
]  # take on tangatial sensors
evoked_tang = evoked.pick_channels(tang_channels)
evoked_tang.plot_joint()
