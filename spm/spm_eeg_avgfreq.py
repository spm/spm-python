from spm._runtime import Runtime


def spm_eeg_avgfreq(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_avgfreq.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_avgfreq", *args, **kwargs)
