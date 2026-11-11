from spm._runtime import Runtime


def spm_NESS_constraints(*args, **kwargs):
    r"""
      constraints on polynomial coefficients of dynamical systems  
        FORMAT [ks,kq,kg,kh] = spm_NESS_constraints(o,A,K,L);  
        o - matrix of orders for polynomial expansion  
        A - adjacency matrix (dynamical coupling)  
        K - upper bound on order for surprisal parameters  
        L - upper bound on order for flow operator parameters (K < L)  
         
        ks  - indices for surprisal   parameters  
        kq  - indices for solenoidal  parameters  
        kg  - indices for dissipative parameters  
        kh  - indices for curvature   parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_NESS_constraints.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_constraints", *args, **kwargs)
