# spm_mne_converter  - a module with converter functions: 1) spm D object to mne.raw object 2) mne.raw to spm D object

import numpy as np

__all__ = [
    "spm_2_mne_raw",
    "mne_raw_2_spm",
]


def spm_2_mne_raw(D):
    """
    Convert an SPM MEEG object (D) to an MNE Raw object.
    This function translates an SPM D object (typically loaded via SPM's MEEG tools in MATLAB or via spm_matlab)
    into an MNE-Python Raw object, preserving channel information, sensor positions, units, and bad channel markings.
    It is intended for use before epoching and has been primarily tested on OPM (Optically Pumped Magnetometer) data.
    Parameters
    ----------
    D : object
        SPM MEEG object (D), expected to provide methods and attributes such as:
            - nchannels(), nsamples(), fsample(), chanlabels(), chantype(), units()
            - sensors(), badchannels(), path()
    Returns
    -------
    raw : mne.io.RawArray
        The corresponding MNE Raw object containing the data and metadata from the SPM D object.
    Notes
    -----
    - Only works before epoching (continuous/pre-epoched data).
    - Channel types and units are mapped from SPM conventions to MNE conventions.
    - Sensor positions and orientations are embedded for MEG and EEG channels.
    - The function attempts to handle the SPM 'tra' matrix for MEG sensor projections.
    - Bad channels are marked in the resulting MNE Raw object.
    - Additional work may be needed for full compatibility with all SPM data types and sensor configurations.
    Examples
    --------
    >>> raw = spm_2_mne_raw(D)
    >>> raw.plot()
    """
    # Converts SPM D object to MNE Raw object
    # importaint: only works before epoching
    # importaint: checked only on opm data

    try:
        import mne
    except ImportError:
        raise ImportError(
            "MNE-Python is required for this function. Please install it using 'pip install mne'."
        )

    n_channels = int(D.nchannels())
    sampling_freq = D.fsample()
    # duration = [float(D.time()[0][0]),float(D.time()[0][-1])]
    n_samples = int(D.nsamples())

    channel_names = list(D.chanlabels())
    type_mapping = {
        "REFMAG": "ref_meg",
        "REFGRAD": "ref_meg",
        "REFPLANAR": "ref_meg",
        "EEG": "eeg",
        "ECG": "ecg",
        "EMG": "emg",
        "LFP": "bio",
        "PHYS": "bio",
        "ILAM": "bio",
        "SRC": "dipole",
        "EOG": "eog",
        "VEOG": "eog",
        "HEOG": "eog",
        "MEG": "mag",
        "MEGMAG": "mag",
        "MEGCOMB": "misc",
        "MEGGRAD": "mag",
        "MEGPLANAR": "grad",
        "TRIG": "stim",
        "Other": "misc",
    }
    channel_types = [type_mapping.get(ch_type, "misc") for ch_type in D.chantype()]
    info = mne.create_info(
        ch_names=channel_names, sfreq=sampling_freq, ch_types=channel_types
    )

    unit_multipliers = {
        "Nan": 1,
        "mT": 10 ** (-3),
        "nT": 10 ** (-9),
        "pT": 10 ** (-12),
        "fT": 10 ** (-15),
        "T": 1,
        "V": 1,
        "mV": 1,
    }

    unit_mul_per_ch = [unit_multipliers[unit] for unit in D.units()]
    data = np.zeros((n_channels, n_samples))
    data[:, :] = D[:, :, :]
    data = np.array(
        [
            channel_data * unit_mul
            for channel_data, unit_mul in zip(data, unit_mul_per_ch)
        ]
    )

    # todo check EEG channels are translating properly
    # sens_ch_start = np.sum([ch_type == 'TRIG' for ch_type in D.chantype()])
    i_meg = 0
    i_eeg = 0
    i_trig = 0
    for i, ch in enumerate(info["chs"]):
        if ch["kind"] == 1:
            k_unit = 10 ** (-3) if D.sensors("MEG").unit == "mm" else 1
            ch["loc"] = np.concatenate(
                (
                    D.sensors("MEG").chanpos[i_meg] * k_unit,
                    D.sensors("MEG").chanori[i_meg],
                    np.zeros(6),
                )
            )
            ch["unit"] = mne.io.constants.FIFF.FIFF_UNIT_T
            ch["unit_mul"] = mne.io.constants.FIFF.FIFF_UNITM_NONE
            ch["range"] = 1.0
            ch["cal"] = 1.0
            ch["coord_frame"] = mne.io.constants.FIFF.FIFFV_COORD_DEVICE
            i_meg += 1
        elif ch["kind"] == 2:  # EEG channels
            ch["loc"] = np.concatenate(
                (D.sensors("EEG").chanpos[i_eeg], np.zeros(9))
            )  # CHECK HOW IT WORKS
            ch["unit"] = (
                mne.io.constants.FIFF.FIFF_UNIT_V
                if D.units()[i_eeg] == "V"
                else mne.io.constants.FIFF.FIFF_UNIT_M
            )
            ch["unit_mul"] = mne.io.constants.FIFF.FIFF_UNITM_NONE
            ch["range"] = 1.0
            ch["cal"] = 1.0
            ch["coord_frame"] = mne.io.constants.FIFF.FIFFV_COORD_HEAD
            i_eeg += 1
        elif ch["kind"] == 3:
            ch["unit"] = (
                mne.io.constants.FIFF.FIFF_UNIT_V
                if D.units()[i_trig] == "V"
                else mne.io.constants.FIFF.FIFF_UNIT_M
            )
            ch["unit_mul"] = mne.io.constants.FIFF.FIFF_UNITM_NONE
            i_trig += 1
    # needs work to embed the tra matrix into prog. for now it is saved separetly for researcher to use for correcting forward model
    if D.sensors("MEG").tra.shape[0] != D.sensors("MEG").tra.shape[1]:
        np.savetxt(
            D.path() + "/tra_matrix_from_spm.tsv", D.sensors("MEG").tra, delimiter="\t"
        )
    else:
        U, S, V = np.linalg.svd(D.sensors("MEG").tra, full_matrices=False)
        rank_tra = np.linalg.matrix_rank(D.sensors("MEG").tra)
        V_real = np.conj(V.T)
        proj_vec = []
        proj_vec = V_real[:, rank_tra:]
        from numpy import arange

        if proj_vec.shape[1] > 0:
            for ii in arange(proj_vec.shape[1]):
                proj_data = dict(
                    col_names=list(D.sensors("MEG").label),
                    row_names=None,
                    data=proj_vec[:, ii].reshape(1, -1),
                    ncol=len(D.sensors("MEG").label),
                    nrow=1,
                )
                info["projs"].append(
                    mne.Projection(
                        active=True,
                        data=proj_data,
                        desc="from matlab tra matrix",
                        kind=1,
                        explained_var=None,
                    )
                )
    # np.savetxt(D.path()+'/tra_matrix_from_spm.tsv', D.sensors('MEG').tra, delimiter='\t')
    bad_channels = D.badchannels()
    if len(bad_channels) > 0:
        info["bads"] = [
            channel_names[int(i - 1)]  # python index = matlab index - 1
            for i in bad_channels
        ]
    raw = mne.io.RawArray(data, info)
    return raw


def mne_raw_2_spm(raw, data_path, file_name=None):
    """Convert MNE raw object to SPM D object.
    Parameters
    ----------
    raw : mne.io.Raw
        MNE raw object.
    data_path : str
        Path to save the SPM D object.
    file_name : str, optional
        Name of the SPM D object file. The default is None, in which case the file name is generated based on the raw object.
    Returns
    -------
    D : spm.meeg
        SPM D object.
    """

    from datetime import datetime
    import os

    try:
        import mne
    except ImportError:
        raise ImportError(
            "MNE-Python is required for this function. Please install it using 'pip install mne'."
        )

    from spm import meeg, Struct

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    os.chdir(data_path)
    if file_name is None:
        file_name = (
            f"data from mne {str(raw.info['meas_date'])[:10]}_{current_time}.dat"
        )

    nChans = raw.info["nchan"]
    nSamples = raw.times.shape[0]
    nTrials = 1
    D = meeg(nChans, nSamples, nTrials)
    D = D.fsample(raw.info["sfreq"])
    D = D.path(str(data_path))
    D = D.chanlabels(D, raw.info["ch_names"])

    type_mapping = {
        mne.io.constants.FIFF.FIFFV_REF_MEG_CH: "ref_meg",
        mne.io.constants.FIFF.FIFFV_EEG_CH: "EEG",
        mne.io.constants.FIFF.FIFFV_ECG_CH: "ECG",
        mne.io.constants.FIFF.FIFFV_EMG_CH: "emg",
        mne.io.constants.FIFF.FIFFV_BIO_CH: "BIO",
        mne.io.constants.FIFF.FIFFV_DIPOLE_WAVE: "dipole",
        mne.io.constants.FIFF.FIFFV_EOG_CH: "EOG",
        mne.io.constants.FIFF.FIFFV_MEG_CH: "MEGMAG",
        mne.io.constants.FIFF.FIFFV_MISC_CH: "misc",
        mne.io.constants.FIFF.FIFFV_STIM_CH: "TRIG",
    }

    chan_types = [type_mapping[ch["kind"]] for ch in raw.info["chs"]]
    D = D.chantype(D, chan_types)

    mapping_units = {
        mne.io.constants.FIFF.FIFF_UNIT_T: "T",  # Reference MEG channels
        mne.io.constants.FIFF.FIFF_UNIT_V: "V",  # EEG channels
        mne.io.constants.FIFF.FIFFV_STIM_CH: "AU",
        mne.io.constants.FIFF.FIFF_UNIT_T_M: "T/m",
    }
    unit_multipliers = {
        mne.io.constants.FIFF.FIFF_UNITM_NONE: "",
        mne.io.constants.FIFF.FIFF_UNITM_M: "m",
        mne.io.constants.FIFF.FIFF_UNITM_M: "micro",
        mne.io.constants.FIFF.FIFF_UNITM_N: "p",
        mne.io.constants.FIFF.FIFF_UNITM_P: "n",
        mne.io.constants.FIFF.FIFF_UNITM_F: "f",
        mne.io.constants.FIFF.FIFF_UNITM_NONE: "",
    }
    chan_units = [
        str(unit_multipliers[ch["unit_mul"]] + mapping_units[ch["unit"]])
        for ch in raw.info["chs"]
    ]
    D = D.units(D, chan_units)

    meg_label = [None] * (chan_types.count("MEGMAG"))
    meg_chanunit = [None] * (chan_types.count("MEGMAG"))
    meg_chantype = [None] * (chan_types.count("MEGMAG"))
    meg_pos = np.zeros(((chan_types.count("MEGMAG")), 3))
    meg_ori = np.zeros(((chan_types.count("MEGMAG")), 3))
    meg_conter = 0
    eeg_label = [None] * (chan_types.count("EEG"))
    eeg_chanunit = [None] * (chan_types.count("EEG"))
    eeg_chantype = [None] * (chan_types.count("EEG"))
    eeg_pos = np.zeros(((chan_types.count("EEG")), 3))
    eeg_ori = np.zeros(((chan_types.count("EEG")), 3))
    eeg_conter = 0
    for i, ch in enumerate(raw.info["chs"]):
        if chan_types[i] == "MEGMAG":
            meg_pos[meg_conter, :] = [ch["loc"][0], ch["loc"][1], ch["loc"][2]]
            meg_ori[meg_conter, :] = [ch["loc"][3], ch["loc"][4], ch["loc"][5]]
            meg_label[meg_conter] = ch["ch_name"]
            meg_chanunit[meg_conter] = str(
                unit_multipliers[ch["unit_mul"]] + mapping_units[ch["unit"]]
            )
            meg_chantype[meg_conter] = type_mapping[ch["kind"]]
            meg_conter += 1
        if chan_types[i] == "EEG":
            eeg_pos[eeg_conter, :] = [ch["loc"][0], ch["loc"][1], ch["loc"][2]]
            eeg_ori[eeg_conter, :] = [ch["loc"][3], ch["loc"][4], ch["loc"][5]]
            eeg_label[eeg_conter] = ch["ch_name"]
            eeg_chanunit[eeg_conter] = str(
                unit_multipliers[ch["unit_mul"]] + mapping_units[ch["unit"]]
            )
            eeg_chantype[eeg_conter] = type_mapping[ch["kind"]]
            eeg_conter += 1

    if meg_conter > 0:
        grad = Struct()
        grad.label = meg_label
        grad.coilpos = np.asarray(meg_pos)
        grad.coilpos = np.asarray(meg_pos)
        grad.coilori = np.asarray(meg_ori)
        grad.coilori = np.asarray(meg_ori)
        grad.chanunit = meg_chanunit
        grad.chantype = meg_chantype

        vec_base = []
        # works oonly when projector is calculated for all the channels
        magnetometer_count = sum(
            1
            for ch in raw.info["chs"]
            if ch["unit"] == mne.io.constants.FIFF.FIFF_UNIT_T
        )
        for ii, proj in enumerate(raw.info["projs"]):
            if proj["data"]["ncol"] == len(meg_label) and proj["active"]:
                vec_base.append(proj["data"]["data"])
        if vec_base == []:
            grad.tra = np.eye(len(meg_label))
        else:
            vec_array = np.array(vec_base).reshape(len(vec_base), magnetometer_count).T
            grad.tra = np.eye(vec_array.shape[0]) - vec_array @ np.linalg.pinv(
                vec_array
            )
        D = D.sensors("MEG", grad)

    if eeg_conter > 0:
        grad = Struct()
        grad.label = eeg_label
        grad.coilpos = np.asarray(eeg_pos)
        grad.coilori = np.asarray(eeg_ori)
        grad.chanunit = eeg_chanunit
        grad.chantype = eeg_chantype

        vec_base = []
        vec_array = []
        eeg_count = sum(
            1
            for ch in raw.info["chs"]
            if ch["kind"] == mne.io.constants.FIFF.FIFFV_EEG_CH
        )
        for ii, proj in enumerate(raw.info["projs"]):
            if proj["data"]["ncol"] == eeg_count and proj["active"]:
                vec_base.append(proj["data"]["data"])
        if vec_base == []:
            grad.tra = np.eye(len(eeg_label))
        else:
            vec_array = np.array(vec_base).reshape(len(vec_base), eeg_count).T
            grad.tra = np.eye(vec_array.shape[0]) - vec_array @ np.linalg.pinv(
                vec_array
            )
        D = D.sensors("EEG", grad)

    D.save()

    D.blank(file_name)
    D = D.link(file_name)
    data = raw.get_data()
    reshaped_data = data.reshape((data.shape[0], data.shape[1], 1))
    D[:, :, :] = reshaped_data

    if len(raw.info["bads"]) == 1:
        D = D.badchannels(raw.info["ch_names"].index(raw.info["bads"][0]), 1)
    elif len(raw.info["bads"]) > 1:
        for i_bad in raw.info["bads"]:
            D = D.badchannels(raw.info["ch_names"].index(i_bad), 1)

    return D
