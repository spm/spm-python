from spm._runtime import Runtime


def spm_fx_Gabor(*args, **kwargs):
    r"""
      state equation for Gabor patches  
        FORMAT [f] = spm_fx_Gabor(x,u,P)  
        x      - state vector  
          x(1) - position  
          x(2) - amplitude  
          x(3) - dispersion  
        u      - input  
          u(1) - position   (forcing)  
          u(2) - amplitude  (forcing)  
          u(3) - dispersion (forcing)  
        f      - dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_Gabor.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_Gabor", *args, **kwargs)
