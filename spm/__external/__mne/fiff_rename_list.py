from mpython import Runtime


def fiff_rename_list(*args, **kwargs):
    """
    fiff_rename_list is a function.
          lst = fiff_rename_list(lst, ch_rename)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_rename_list.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_rename_list", *args, **kwargs)
