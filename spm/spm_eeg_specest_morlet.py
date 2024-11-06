from spm.__wrapper__ import Runtime


def spm_eeg_specest_morlet(*args, **kwargs):
    """
      Plugin for spm_eeg_tf implementing Morlet wavelet transform  
        FORMAT res = spm_eeg_specest_morlet(S, data, time)  
         
        S                     - input structure  
        fields of S:  
           S.subsample   - factor by which to subsample the time axis (default - 1)  
         either  
           S.ncycles     - Morlet wavelet factor (default - 7)  
         or  
           S.timeres     - Fixed time window length in ms  
         
           S.frequencies - vector of frequencies (default - 0-48) at optimal frequency bins  
                                     
        Output:  
         res -   
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             res.fourier - the complex output of wavelet transform  
             res.time    - time axis  
             res.freq    - frequency axis  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_specest_morlet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_specest_morlet", *args, **kwargs)
