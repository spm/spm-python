from spm.__wrapper__ import Runtime


def spm_NESS_constraints(*args, **kwargs):
    """
      constraints on polynomial coefficients or dynamical systems  
        FORMAT [ks,kq,kg,kh] = spm_NESS_constraints(o,A,K,L);  
        o - matrix of orders for polynomial expansion  
        A - adjacency matrix (dynamical coupling)  
        K - upper bound on order for surprisal parameters  
        J - upper bound on order for flow operator parameters  
         
        ks  - indices for surprisal   parameters  
        kq  - indices for solenoidal  parameters  
        kg  - indices for dissipative parameters  
        kh  - indices for curvature   parameters  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_NESS_constraints.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_NESS_constraints", *args, **kwargs)
