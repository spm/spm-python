from spm.__wrapper__ import Runtime


def spm_eeg_recode_epoched_ctf(*args, **kwargs):
    """
      Temporary solution for using trial labels in epoched CTF dataset  
        FORMAT  D = spm_eeg_recode_epoched_ctf(S)  
         
        S                    - input structure (optional)  
        (optional) fields of S:  
                 .D       - converted epoched CTF dataset  
         
        Output:  
        D                 - MEEG object relabeled trials (also saved to disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_recode_epoched_ctf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_recode_epoched_ctf", *args, **kwargs)
