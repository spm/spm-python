from spm._runtime import Runtime


def DEM_demo_Lorenz(*args, **kwargs):
    r"""
      Demo for a Lorentz attractor: In this example we show that DEM and  
        Bayesian filtering can estimate the hidden states of an autonomous system  
        showing deterministic chaos.  Although all schemes perform well given the  
        correct starting values of the hidden states; DEM is the only scheme that  
        can re-capture the true trajectory without them.  this is because DEM   
        represents generalised coordinates, in which the dynamics unfold.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_Lorenz.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_Lorenz", *args, **kwargs, nargout=0)
