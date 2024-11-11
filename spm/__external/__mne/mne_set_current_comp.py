from spm.__wrapper__ import Runtime


def mne_set_current_comp(*args, **kwargs):
    """
       
        mne_set_current_comp(chs,value)  
         
        Set the current compensation value in the channel info structures  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_set_current_comp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_set_current_comp", *args, **kwargs)
