from spm._runtime import Runtime


def spm_eeg_tms_correct(*args, **kwargs):
    r"""
      Function for removing TMS artefacts  
        FORMAT D = spm_eeg_tms_correct(S)  
        S                    - input structure (optional)  
        (optional) fields of S:  
          S.D                - MEEG object or filename of M/EEG mat-file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_tms_correct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_tms_correct", *args, **kwargs)
