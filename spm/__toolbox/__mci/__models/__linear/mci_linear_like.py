from spm._runtime import Runtime


def mci_linear_like(*args, **kwargs):
    r"""
      Compute log likelihood of linear model  
        FORMAT [L,E,st] = mci_linear_like (theta,M,U,Y)  
         
        theta     regression coefficients  
        M         model  
        U         inputs  
        Y         data  
          
        L         Log likelihood  
        E         Errors  
        st        Status flag (0 for OK, -1 for problem)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/linear/mci_linear_like.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linear_like", *args, **kwargs)
