from spm.__wrapper__ import Runtime


def spm_ness_m2S(*args, **kwargs):
    """
      Conditional moments of a Gaussian density (polynomial parameterisation)  
        FORMAT [p0,X,F,f,NESS] = spm_ness_hd(M,x)  
       --------------------------------------------------------------------------  
        m  - (Conditional) mean  
        C  - (Conditional) covariance  
         
        Sp - Polynomial coefficients or parameters of log density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_m2S.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ness_m2S", *args, **kwargs)
