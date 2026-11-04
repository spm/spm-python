from spm._runtime import Runtime


def spm_eeg_inv_forward(*args, **kwargs):
    r"""
      Compute M/EEG leadfield  
        FORMAT D = spm_eeg_inv_forward(D,val)  
         
        D                - input struct  
        (optional) fields of S:  
        D                - filename of EEG/MEG mat-file  
         
        Output:  
        D                - EEG/MEG struct with filenames of Gain matrices)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_forward.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_forward", *args, **kwargs)
