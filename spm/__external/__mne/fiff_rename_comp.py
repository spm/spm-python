from spm._runtime import Runtime


def fiff_rename_comp(*args, **kwargs):
    r"""
    fiff_rename_comp is a function.  
          comp = fiff_rename_comp(comp, ch_rename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_rename_comp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_rename_comp", *args, **kwargs)
