from spm._runtime import Runtime


def spm_dcm_KL(*args, **kwargs):
    r"""
      Compute the distance between two models based on prior responses  
        FORMAT [D,C,K] = spm_dcm_KL(Mi,Mj)  
         
        M{1:n}   - structure array of models  
         
        D(n x n) - distance matrix (KL divergence)  
        C{1:n}   - response covariances  
        K{1:n}   - response means  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_KL.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_KL", *args, **kwargs)
