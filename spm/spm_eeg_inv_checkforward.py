from spm._runtime import Runtime


def spm_eeg_inv_checkforward(*args, **kwargs):
    r"""
      Check M/EEG forward model  
        FORMAT spm_eeg_inv_checkforward(D, val, ind)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_checkforward.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_checkforward", *args, **kwargs, nargout=0)
