from spm._runtime import Runtime


def spm_ness_m2S(*args, **kwargs):
    r"""
      Conditional moments of a Gaussian density (polynomial parameterisation)  
        FORMAT [p0,X,F,f,NESS] = spm_ness_hd(M,x)  
       --------------------------------------------------------------------------  
        m  - (Conditional) mean  
        C  - (Conditional) covariance  
         
        Sp - Polynomial coefficients or parameters of log density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_m2S.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_m2S", *args, **kwargs)
