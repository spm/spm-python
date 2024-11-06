from spm.__wrapper__ import Runtime


def spm_eeg_invert_ui(*args, **kwargs):
    """
      GUI for ReML inversion of forward model for EEG-MEG  
        FORMAT [D] = spm_eeg_invert_ui(D,val)  
        ReML estimation of regularisation hyperparameters using the  
        spatio-temporal hierarchy implicit in EEG data  
        sets:  
         
            D.inv{i}.inverse.trials - trials (in D.events.types) to invert  
            D.inv{i}.inverse.smooth - smoothness of source priors (mm)  
            D.inv{i}.inverse.type   - 'MSP' multiple sparse priors  
                                      'LOR' LORETA-like model  
                                      'IID' LORETA and WMN  
            D.inv{i}.inverse.xyz    - (n x 3) locations of spherical VOIs  
            D.inv{i}.inverse.rad    - radius (mm) of VOIs  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_ui", *args, **kwargs)
