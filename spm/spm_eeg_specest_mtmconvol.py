from spm.__wrapper__ import Runtime


def spm_eeg_specest_mtmconvol(*args, **kwargs):
    """
      Plugin for spm_eeg_tf implementing spectral estimation using Fieldtrip's freqanalysis_mtmconvol  
        FORMAT res = spm_eeg_specest_mtmconvol(S, data, time)  
         
        S                     - input structure  
        fields of S:  
           S.taper       - taper to use ('hanning', 'rectwin', 'dpss', 'sine' or  
                           other possible inputs of 'window'  
           S.freqres     - frequency resolutions (plus-minus for each frequency, can  
                           be a vector with a value per frequency)  
           S.frequencies - vector of frequencies  
           S.timeres     - time resolution in ms (length of the sliding time-window)  
           S.timestep    - time step (in ms) to slide the time-window by.  
         
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided:  
             res.fourier - the complex output of wavelet transform (in the case  
                           of single taper)  
             res.pow     - power (in case of multiple tapers, phase is not computed)  
             res.time    - time axis  
             res.freq    - frequency axis  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_specest_mtmconvol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_specest_mtmconvol", *args, **kwargs)
