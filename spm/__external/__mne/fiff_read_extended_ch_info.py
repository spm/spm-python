from spm._runtime import Runtime


def fiff_read_extended_ch_info(*args, **kwargs):
    r"""
    fiff_read_extended_ch_info is a function.  
          [chs, ch_rename] = fiff_read_extended_ch_info(chs, meas_info, fid)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_extended_ch_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_extended_ch_info", *args, **kwargs)
