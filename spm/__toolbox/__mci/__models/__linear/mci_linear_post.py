from spm._runtime import Runtime


def mci_linear_post(*args, **kwargs):
    r"""
      Analytic posterior for linear regression  
        FORMAT [Ep,Cp,L] = mci_linear_post (M,U,Y)  
          
        M     Model Structure  
        U     Inputs  
        Y     Data  
         
        Ep    Posterior mean  
        Cp    Posterior covariance  
        L     Log evidence  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/linear/mci_linear_post.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linear_post", *args, **kwargs)
