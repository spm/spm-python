from spm.__wrapper__ import Runtime


def spm_fx_Gabor(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_Gabor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_Gabor", *args, **kwargs)
