from spm._runtime import Runtime


def spm_gx_SHC(*args, **kwargs):
    r"""
      maps to state of a SCH to a 2-D position in the world  
        FORMAT [g] = spm_gx_SHC(x,v,P)  
         
        x    - vector of hidden sates  
        P.g  - state-space location associated with each hidden states  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_SHC.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_SHC", *args, **kwargs)
