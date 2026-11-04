from spm._runtime import Runtime


def spm_nwpost(*args, **kwargs):
    r"""
      Get posterior distribution over m,Lambda  
        FORMAT [M] = spm_nwpost (M,w)  
         
        M     M.prior - params of Normal-Wishart prior  
        w     Multivariate data samples  
         
        M     M.post - params of Normal-Wishart posterior  
         
        Bernardo and Smith, Bayesian Theory, 2000 (p.441)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_nwpost.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_nwpost", *args, **kwargs)
