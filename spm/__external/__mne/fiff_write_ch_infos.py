from spm._runtime import Runtime


def fiff_write_ch_infos(*args, **kwargs):
    r"""
    fiff_write_ch_infos is a function.  
          cals = fiff_write_ch_infos(fid, chs, reset_range, ch_rename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_ch_infos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_ch_infos", *args, **kwargs)
