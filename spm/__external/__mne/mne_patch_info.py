from mpython import Runtime


def mne_patch_info(*args, **kwargs):
    """

        [pinfo] = mne_patch_info(nearest)

        Generate the patch information from the 'nearest' vector in a source space


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_patch_info.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_patch_info", *args, **kwargs)
