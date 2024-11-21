from spm.__wrapper__ import Runtime


def spm_eeg_cont_power(*args, **kwargs):
    """
      Compute power of continuous M/EEG data  
        FORMAT D = spm_eeg_cont_power(S)  
         
        This function computes power from band-pass filtered data using hilbert  
        transform. Can also be used as a template for any kind of computation on  
        continuous data.  
         
        S           - input structure (optional)  
        (optional) fields of S:  
          S.D       - MEEG object or filename of M/EEG mat-file  
         
        D           - MEEG object (also written to disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_cont_power.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_cont_power", *args, **kwargs)
