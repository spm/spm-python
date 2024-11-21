from spm.__wrapper__ import Runtime


def DEM_demo_double_well(*args, **kwargs):
    """
      DEMO comparing DEM with particle filtering in the context of a bimodal  
        conditional density.  This demonstrates a shortcoming of DEM in that it  
        fails to represent the true density.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_double_well.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_double_well", *args, **kwargs, nargout=0)
