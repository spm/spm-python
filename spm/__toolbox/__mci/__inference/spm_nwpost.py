from spm.__wrapper__ import Runtime


def spm_nwpost(*args, **kwargs):
    """
      Get posterior distribution over m,Lambda  
        FORMAT [M] = spm_nwpost (M,w)  
         
        M     M.prior - params of Normal-Wishart prior  
        w     Multivariate data samples  
         
        M     M.post - params of Normal-Wishart posterior  
         
        Bernardo and Smith, Bayesian Theory, 2000 (p.441)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_nwpost.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nwpost", *args, **kwargs)
