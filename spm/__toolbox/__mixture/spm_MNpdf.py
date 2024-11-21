from spm.__wrapper__ import Runtime


def spm_MNpdf(*args, **kwargs):
    """
      Evaluate a Multivariate Gaussian PDF  
        FORMAT [y] = spm_MNpdf (m, C, x)  
          
        m     [d x 1] mean  
        C     [d x d] covar  
        x     [n x d] points at which to evaluate  
         
        y     [n x 1] density at n points  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_MNpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MNpdf", *args, **kwargs)
