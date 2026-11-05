from spm._runtime import Runtime


def DEM_COVID_MASKS(*args, **kwargs):
    r"""
      Returns the probability of mask wearing at a particular day  
        FORMAT [X] = DEM_COVID_MASKS(i)  
        = datenum('dd-mmm-yyyy')  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_COVID_MASKS.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_COVID_MASKS", *args, **kwargs)
