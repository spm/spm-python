from spm._runtime import Runtime


def spm_eeg_cont_power(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_cont_power.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_cont_power", *args, **kwargs)
