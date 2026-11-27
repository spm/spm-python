from spm._runtime import Runtime


def mci_logistic_like(*args, **kwargs):
    r"""
      Compute log likelihood of logistic model  
        FORMAT [L,E,st] = mci_logistic_like (P,M,U,Y)  
         
        P         parameters  
        M         model  
        U         inputs  
        Y         data  
          
        L         Log likelihood  
        E         Errors  
        st        Status flag (0 for OK, -1 for problem)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/logistic/mci_logistic_like.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_logistic_like", *args, **kwargs)
