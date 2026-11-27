from spm._runtime import Runtime


def spm_fx_mountaincar_Q(*args, **kwargs):
    r"""
      state equations based on the Helmholtz decomposition  
        FORMAT f = spm_fx_mountaincar_Q(x,v,P)  
        x    - [x, x']  
        v    - exogenous force  
         
        P.a  - 0th order coefficients of Q  
        P.b  - 1st order coefficients of Q  
        P.c  - 2nd order coefficients of Q  
         
        M    - model structure  
         
        f    - flow dx/dt  
         
        see:  
        Gaussian Processes in Reinforcement Learning  
        Carl Edward Rasmussen and Malte Kuss  
        Max Planck Institute for Biological Cybernetics  
        Spemannstraße 38, 72076 Tubingen, Germany  
        {carl,malte.kuss}@tuebingen.mpg.de  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_mountaincar_Q.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_mountaincar_Q", *args, **kwargs)
