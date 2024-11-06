from spm.__wrapper__ import Runtime


def spm_eeg_inv_get_vol_sens(*args, **kwargs):
    """
      Retrieves data for leadfield computation from D.inv structure  
        FORMAT data = spm_eeg_inv_get_vol_sens(D, val, space, gradsource, modality)  
           D   -  @meeg object  
           val - inversion index (overrides D.val)  
           space - one of 'MNI-aligned', 'Head', 'Native' (default 'MNI-aligned')  
           gradsource - 'inv' (default) to get MEG grad from D.inv  
                        otherwise from D.sensors (useful for reusing head-models  
                        for different runs in the same session)  
           modality - 'EEG' or 'MEG' to force only one modality for multimodal  
                       datasets  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_get_vol_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_get_vol_sens", *args, **kwargs)
