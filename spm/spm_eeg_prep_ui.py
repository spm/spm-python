from spm._runtime import Runtime


def spm_eeg_prep_ui(*args, **kwargs):
    r"""
      User interface for spm_eeg_prep function performing several tasks  
        for preparation of converted MEEG data for further analysis  
        FORMAT spm_eeg_prep_ui(callback)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_prep_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_prep_ui", *args, **kwargs, nargout=0)
