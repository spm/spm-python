from spm._runtime import Runtime


def spm_eeg_inv_check(*args, **kwargs):
    r"""
      Checks that the EEG/MEG .mat file structure is loaded properly and that  
        the particular inversion of interest has been specified  
         
        FORMAT [D,val] = spm_eeg_inv_check(D,[val])  
        Input:  
        S              - data structure or its filename  
        val            - model of interest (usually 1)  
        Output:  
        D              - data structure  
        val            - model of interest D.val  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_check.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_check", *args, **kwargs)
