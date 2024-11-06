from spm.__wrapper__ import Runtime


def spm_Dpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of Dirichlet distribution  
        FORMAT f = spm_Dpdf(x,a)  
          
        x - Dirichlet variate  
        a - Dirichlet parameters (a>0)  
        f - PDF of Dirichlet-distribution at point x  
       __________________________________________________________________________  
         
        spm_Dpdf implements the Probability Density Function for Dirichlet   
        distribution.  
         
        Definition:  
       --------------------------------------------------------------------------  
        See http://en.wikipedia.org/wiki/Dirichlet_distribution  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Direct computation using logs and MATLAB's implementation of the log of   
        the gamma function (gammaln).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Dpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Dpdf", *args, **kwargs)
