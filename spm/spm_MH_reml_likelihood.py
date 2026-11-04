from spm._runtime import Runtime


def spm_MH_reml_likelihood(*args, **kwargs):
    r"""
      Likelihood function for spm_MH_reml  
        FORMAT [L] = spm_MH_reml_likelihood(h,Y,M)  
         
        h - hyperparameters  
        Y - residual covariance  
         
        L - likelihood p(Y,P)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MH_reml_likelihood.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MH_reml_likelihood", *args, **kwargs)
