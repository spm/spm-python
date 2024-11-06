from spm.__wrapper__ import Runtime


def DEM_demo_convolution(*args, **kwargs):
    """
      DEM demo for linear deconvolution:  This demo considers the deconvolution  
        of the responses of a single-input-multiple output input-state-output  
        model (DCM) to disclose the input or causes.  It focuses on estimating the  
        causes and hidden states: The notes provide a comparative evaluation with   
        extended Kalman filtering (see script after return).  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_convolution.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_convolution", *args, **kwargs, nargout=0)
