from spm._runtime import Runtime


def spm_eeg_review_callbacks(*args, **kwargs):
    """
      Callbacks of the M/EEG Review facility  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_review_callbacks.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_review_callbacks", *args, **kwargs)
