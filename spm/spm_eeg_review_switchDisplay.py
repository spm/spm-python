from spm.__wrapper__ import Runtime


def spm_eeg_review_switchDisplay(*args, **kwargs):
    """
      Switch between displays in the M/EEG Review facility  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_review_switchDisplay.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_review_switchDisplay", *args, **kwargs)
