from spm.__wrapper__ import Runtime


def spm_dexpm(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_dexpm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dexpm", *args, **kwargs)
