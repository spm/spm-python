from spm._runtime import Runtime


def DEM_demo_convolution(*args, **kwargs):
    r"""
      DEM demo for linear deconvolution:  This demo considers the deconvolution  
        of the responses of a single-input-multiple output input-state-output  
        model (DCM) to disclose the input or causes.  It focuses on estimating the  
        causes and hidden states: The notes provide a comparative evaluation with   
        extended Kalman filtering (see script after return).  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_convolution.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_convolution", *args, **kwargs, nargout=0)
