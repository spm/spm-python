from spm._runtime import Runtime


def DEM_ness_Lap(*args, **kwargs):
    r"""
      Nonequilibrium steady-state under a Helmholtz decomposition  
        FORMAT DEM_ness_Lap  
       --------------------------------------------------------------------------  
        This demonstration routine illustrates the use of generalised  
        (variational) filtering to invert a generic model of any complex  
        dynamical system. This model makes the minimal assumption that there  
        exists a nonequilibrium steady-state (i.e., a pullback attractor). The  
        ensuing solution to the density dynamics—under the Helmholtz-Hodge  
        decomposition—furnishes a normal form for the flow or dynamics. This  
        normal form can be parameterised to 2nd order in terms of (solenoidal and  
        dissipative) flow operators that operate on the gradients of the system’s  
        potential, surprisal or self-information (i.e., the implausibility of  
        being found in any given state and the NESS density). The second order  
        parameterisation (of the underlying flow) is used as a generative model  
        to learn the parameters of the system.  
         
        This enables forecasting; in the sense that the system can be solved for  
        future time points (with random fluctuations on the flow) to produce an  
        ensemble or sample estimate of future states.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_ness_Lap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_ness_Lap", *args, **kwargs, nargout=0)
