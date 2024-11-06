from spm.__wrapper__ import Runtime


def mne_get_current_comp(*args, **kwargs):
    """
       
        [comp] = mne_get_current_comp(info)  
         
        Get the current compensation in effect in the data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_get_current_comp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_get_current_comp", *args, **kwargs)
