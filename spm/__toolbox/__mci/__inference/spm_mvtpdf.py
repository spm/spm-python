from spm.__wrapper__ import Runtime


def spm_mvtpdf(*args, **kwargs):
    """
      PDF of multivariate T-distribution  
        FORMAT [p] = spm_mvtpdf (x,mu,Lambda,v)  
         
        x      - ordinates [d x N]  
        mu     - mean [d x 1]  
        Lambda - precision matrix [d x d]  
        v      - degrees of freedom  
         
        p      - probability density  
         
        See J. Bernardo and A. Smith (2000)   
        Bayesian Theory, Wiley (page 435)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mvtpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvtpdf", *args, **kwargs)
