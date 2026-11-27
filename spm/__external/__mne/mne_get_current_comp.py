from spm._runtime import Runtime


def mne_get_current_comp(*args, **kwargs):
    r"""
       
        [comp] = mne_get_current_comp(info)  
         
        Get the current compensation in effect in the data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_get_current_comp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_get_current_comp", *args, **kwargs)
