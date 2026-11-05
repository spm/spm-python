from spm._runtime import Runtime


def spm_eeg_recode_epoched_ctf(*args, **kwargs):
    r"""
      Temporary solution for using trial labels in epoched CTF dataset  
        FORMAT  D = spm_eeg_recode_epoched_ctf(S)  
         
        S                    - input structure (optional)  
        (optional) fields of S:  
                 .D       - converted epoched CTF dataset  
         
        Output:  
        D                 - MEEG object relabeled trials (also saved to disk)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_recode_epoched_ctf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_recode_epoched_ctf", *args, **kwargs)
