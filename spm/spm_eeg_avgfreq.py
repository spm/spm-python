from spm.__wrapper__ import Runtime


def spm_eeg_avgfreq(*args, **kwargs):
    """
      Average a TF-dataset over frequency to get a time-domain dataset  
        FORMAT D = spm_eeg_avgfreq(S)  
         
        S        - input struct  
         fields of S:  
          D        - MEEG object or filename of M/EEG mat-file with epoched data  
          freqwin  - frequency window to average over [default: [-Inf, Inf]]  
          prefix   - prefix for the output file [default: 'P']  
         
        Output:  
        D        - MEEG object  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_avgfreq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_avgfreq", *args, **kwargs)
