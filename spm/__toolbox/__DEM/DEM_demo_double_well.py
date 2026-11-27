from spm._runtime import Runtime


def DEM_demo_double_well(*args, **kwargs):
    r"""
      DEMO comparing DEM with particle filtering in the context of a bimodal  
        conditional density.  This demonstrates a shortcoming of DEM in that it  
        fails to represent the true density.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_double_well.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_double_well", *args, **kwargs, nargout=0)
