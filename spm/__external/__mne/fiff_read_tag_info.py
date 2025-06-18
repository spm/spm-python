from mpython import Runtime


def fiff_read_tag_info(*args, **kwargs):
    """

        [fid,dir] = fiff_open(fname)

        Open a fif file and provide the directory of tags


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_tag_info.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_tag_info", *args, **kwargs)
