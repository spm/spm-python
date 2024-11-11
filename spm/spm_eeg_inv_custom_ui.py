from spm.__wrapper__ import Runtime


def spm_eeg_inv_custom_ui(*args, **kwargs):
    """
      GUI for parameters of inversion of forward model for EEG-MEG  
        FORMAT [inverse] = spm_eeg_inv_custom_ui(D)  
         
        D  - M/EEG data structure  
         
        gets:  
         
            inverse.type   - 'GS' Greedy search on MSPs  
                             'ARD' ARD search on MSPs  
                             'LOR' LORETA-like model  
                             'IID' LORETA and minimum norm  
            inverse.woi    - time window of interest ([start stop] in ms)  
            inverse.Han    - switch for Hanning window  
            inverse.lpf    - band-pass filter - low frequency cut-off (Hz)  
            inverse.hpf    - band-pass filter - high frequency cut-off (Hz)  
            inverse.pQ     - any source priors (eg from fMRI) - cell array  
            inverse.xyz    - (n x 3) locations of spherical VOIs  
            inverse.rad    - radius (mm) of VOIs  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_custom_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_custom_ui", *args, **kwargs)
