from spm.__wrapper__ import Runtime


def DEM_demo_hdm(*args, **kwargs):
    """
      demo for Hemodynamic deconvolution  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_hdm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_hdm", *args, **kwargs, nargout=0)
