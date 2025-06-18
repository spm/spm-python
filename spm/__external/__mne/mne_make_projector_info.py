from mpython import Runtime


def mne_make_projector_info(*args, **kwargs):
    """

        [proj,nproj] = mne_make_projector_info(info)

        Make an SSP operator using the meas info


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_make_projector_info.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_make_projector_info", *args, **kwargs)
