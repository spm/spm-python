from spm._runtime import Runtime


def spm_gx_Gabor(*args, **kwargs):
    r"""
      observer equation for Gabor patches  
        FORMAT [g] = spm_gx_Gabor(x,u,P)  
        x      - state vector  
          x(1) - position  
          x(2) - amplitude  
          x(3) - dispersion  
        u      - input  
          u(1) - position  (forcing)  
          u(2) - amplitude (forcing)  
          u(3) - width (forcing)  
        f      - dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_Gabor.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_Gabor", *args, **kwargs)
