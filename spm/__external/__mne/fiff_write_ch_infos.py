from spm._runtime import Runtime


def fiff_write_ch_infos(*args, **kwargs):
    """
    fiff_write_ch_infos is a function.  
          cals = fiff_write_ch_infos(fid, chs, reset_range, ch_rename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_ch_infos.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_ch_infos", *args, **kwargs)
