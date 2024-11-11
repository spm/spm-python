from spm.__wrapper__ import Runtime


def spm_DEM_int(*args, **kwargs):
    """
      Integrate/evaluate a hierarchical model given innovations z{i} and w{i}  
        FORMAT [V,X,Z,W] = spm_DEM_int(M,z,w,c)  
         
        M{i}    - model structure  
        z{i}    - innovations (causes)  
        w{i}    - innovations (states)  
        c{i}    - exogenous causes  
         
        V{i}    - causal states (V{1} = y = response)  
        X{i}    - hidden states  
        Z{i}    - fluctuations (causes)  
        W{i}    - fluctuations (states)  
         
        The system is evaluated at the prior expectation of the parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_int.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_int", *args, **kwargs)
