from spm._runtime import Runtime


def mne_set_current_comp(*args, **kwargs):
    r"""
       
        mne_set_current_comp(chs,value)  
         
        Set the current compensation value in the channel info structures  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_set_current_comp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_set_current_comp", *args, **kwargs)
