from mpython import Runtime


def fiff_read_extended_ch_info(*args, **kwargs):
    """
    fiff_read_extended_ch_info is a function.
          [chs, ch_rename] = fiff_read_extended_ch_info(chs, meas_info, fid)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_extended_ch_info.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_extended_ch_info", *args, **kwargs)
