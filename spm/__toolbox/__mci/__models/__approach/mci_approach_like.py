from spm.__wrapper__ import Runtime


def mci_approach_like(*args, **kwargs):
    """
      Log-likelihood for approach model   
        FORMAT [L,yhat,st] = mci_approach_like (P,M,U,Y)  
         
        P         parameters  
        M,U,Y     as usual  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_like.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_approach_like", *args, **kwargs)
