from mpython import Runtime


def fiff_make_ch_rename(*args, **kwargs):
    """
    fiff_make_ch_rename is a function.
          ch_rename = fiff_make_ch_rename(chs)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_make_ch_rename.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_make_ch_rename", *args, **kwargs)
