from spm.__wrapper__ import Runtime


def spm_eeg_specest_hilbert(*args, **kwargs):
    """
      Plugin for spm_eeg_tf implementing spectral estimation using Hilbert transform  
        FORMAT res = spm_eeg_specest_hilbert(S, data, time)  
         
        S                     - input structure  
        fields of S:  
           S.subsample   - factor by which to subsample the time axis (default - 1)  
           S.freqres     - frequency resolutions (plus-minus for each frequency, can  
                           be a vector with a value per frequency)  
           S.frequencies - vector of frequencies  
           S.order       - butterworth filter order (can be a vector with a value  
                           per frequency)  
         
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             res.fourier - the complex output of wavelet transform  
             res.time    - time axis  
             res.freq    - frequency axis  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_specest_hilbert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_specest_hilbert", *args, **kwargs)
