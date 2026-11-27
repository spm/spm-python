from spm._runtime import Runtime


def spm_eeg_regressors_movement_ctf(*args, **kwargs):
    r"""
      Generate movement regressors for CTF MEG data  
        FORMAT res = spm_eeg_regressors_movement_ctf(S)  
        S                     - input structure  
        fields of S:  
           S.D                - M/EEG object  
         
           Additional parameters can be defined specific for each plugin  
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided the plugin returns  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_regressors_movement_ctf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_regressors_movement_ctf", *args, **kwargs)
