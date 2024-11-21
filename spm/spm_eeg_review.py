from spm.__wrapper__ import Runtime


def spm_eeg_review(*args, **kwargs):
    """
      General review (display) of SPM meeg object  
        FORMAT spm_eeg_review(D,flags,inv)  
         
        INPUT:  
        D      - meeg object  
        flag   - switch to any of the displays (optional)  
        inv    - which source reconstruction to display (when called from  
        spm_eeg_inv_imag_api.m)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_review.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_review", *args, **kwargs, nargout=0)
