from spm._runtime import Runtime


def DEM_demo_hdm(*args, **kwargs):
    r"""
      demo for Hemodynamic deconvolution  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_hdm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_hdm", *args, **kwargs, nargout=0)
