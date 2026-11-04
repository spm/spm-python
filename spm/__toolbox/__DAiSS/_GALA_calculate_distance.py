from spm._runtime import Runtime


def _GALA_calculate_distance(*args, **kwargs):
    r"""
    GALA_calculate_distance is a function.  
          distance = GALA_calculate_distance(mesh)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/GALA_calculate_distance.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_calculate_distance", *args, **kwargs)
