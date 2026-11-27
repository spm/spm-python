from spm._runtime import Runtime


def spm_eeg_review(*args, **kwargs):
    r"""
      General review (display) of SPM meeg object  
        FORMAT spm_eeg_review(D,flags,inv)  
         
        INPUT:  
        D      - meeg object  
        flag   - switch to any of the displays (optional)  
        inv    - which source reconstruction to display (when called from  
        spm_eeg_inv_imag_api.m)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_review.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_review", *args, **kwargs, nargout=0)
