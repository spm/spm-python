from spm._runtime import Runtime


def spm_eeg_review_callbacks(*args, **kwargs):
    r"""
      Callbacks of the M/EEG Review facility  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_review_callbacks.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_review_callbacks", *args, **kwargs)
