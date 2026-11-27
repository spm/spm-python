from spm._runtime import Runtime


def mci_approach_like(*args, **kwargs):
    r"""
      Log-likelihood for approach model   
        FORMAT [L,yhat,st] = mci_approach_like (P,M,U,Y)  
         
        P         parameters  
        M,U,Y     as usual  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/approach/mci_approach_like.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_approach_like", *args, **kwargs)
