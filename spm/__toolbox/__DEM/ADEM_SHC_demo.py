from spm._runtime import Runtime


def ADEM_SHC_demo(*args, **kwargs):
    r"""
      This demo illustrates the use of Lotka-Volterra form SHCs (Stable  
        heteroclinic channel) to prescribe active sampling (inference). In this  
        example each (unstable) fixed point in the SHC attracts the agent to  
        points on the circumference of a circle.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_SHC_demo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_SHC_demo", *args, **kwargs, nargout=0)
