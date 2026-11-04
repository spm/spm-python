from spm._runtime import Runtime


def spm_dexpm(*args, **kwargs):
    r"""
      Differentiate a matrix exponential  
        FORMAT [E,dE] = spm_dexpm(A,dA)  
        A  - Lie algebra  
        dA - basis function to differentiate with respect to  
         
        E  - expm(A)  
        dE - (expm(A+eps*dA)-expm(A-eps*dA))/(2*eps)  
         
        Note that the algorithm is a bit slow, and should perhaps be re-written  
        to use eg scaling and squaring (see Moler's dubious matrix exponentials  
        paper).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Longitudinal/spm_dexpm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dexpm", *args, **kwargs)
