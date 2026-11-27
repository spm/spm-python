from spm._runtime import Runtime


def spm_MNpdf(*args, **kwargs):
    r"""
      Evaluate a Multivariate Gaussian PDF  
        FORMAT [y] = spm_MNpdf (m, C, x)  
          
        m     [d x 1] mean  
        C     [d x d] covar  
        x     [n x d] points at which to evaluate  
         
        y     [n x 1] density at n points  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mixture/spm_MNpdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MNpdf", *args, **kwargs)
