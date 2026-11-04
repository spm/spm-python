from spm._runtime import Runtime


def fiff_rename_list(*args, **kwargs):
    r"""
    fiff_rename_list is a function.  
          lst = fiff_rename_list(lst, ch_rename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_rename_list.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_rename_list", *args, **kwargs)
