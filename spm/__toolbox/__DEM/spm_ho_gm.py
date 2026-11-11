from spm._runtime import Runtime


def spm_ho_gm(*args, **kwargs):
    r"""
      General Gaussian mixture model with derivatives  
        FORMAT Y = spm_ho_poly(P,M,U)  
         
        P    - polynomial parameters (P{i} = i-th order coefficients)  
        M    - model structure  
        U    - (m,n) inputs  
         
        Y(i) =  P{1} + P{2}*U(:,i) + P{3}*kron(U(:,i),U(:,i)) + ...  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_ho_gm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ho_gm", *args, **kwargs)
