from spm.__wrapper__ import Runtime


def spm_eeg_ft_multitaper_coherence(*args, **kwargs):
    """
      Function for computing time-frequency decomposition using multitaper  
         
        WARNING: This function uses some quite specific settings and is not generic. It is  
        just an example of how Fieldtrip spectral analysis can be combined with  
        SPM  
         
        FORMAT D = spm_eeg_ft_multitaper_coherence(S)  
         
        S           - input structure (optional)  
        (optional) fields of S:  
          S.D        - filename, or M/EEG object  
          S.chancomb - Nx2 cell array with channel pairs  
          S.pretrig  - time to start TF analysis in PST (ms)  
          S.posttrig - time to end TF analysis in PST (ms)  
          S.timewin  - time window (resolution) in ms  
          S.timestep - time step in ms  
          S.freqwin  - frequency window (Hz)  
          S.freqres  - frequency resolution  
          S.robust      - (optional) - use robust averaging for computing  
                                       coherence  
                        .savew  - save the weights in an additional dataset  
                        .bycondition - compute the weights by condition (1,  
                                       default) or from all trials (0)  
                        .ks     - offset of the weighting function (default: 3)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_multitaper_coherence.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_ft_multitaper_coherence", *args, **kwargs)
