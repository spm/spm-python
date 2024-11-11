from spm.__wrapper__ import Runtime


def spm_eeg_tms_correct(*args, **kwargs):
    """
      Function for removing TMS artefacts  
        FORMAT D = spm_eeg_tms_correct(S)  
        S                    - input structure (optional)  
        (optional) fields of S:  
          S.D                - MEEG object or filename of M/EEG mat-file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_tms_correct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_tms_correct", *args, **kwargs)
