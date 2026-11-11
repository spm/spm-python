from spm._runtime import Runtime


def pm_diff(*args, **kwargs):
    r"""
      Calculate derivative in one direction of volume (matrix or memory mapped)  
        FORMAT D = pm_diff(V,dir)  
        V    - 3D array, or filestruct returned from spm_vol  
        dir  - direction (1, 2 or 3 for x, y or z respectively)  
         
        D    - 3D array of derivatives  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/FieldMap/pm_diff.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pm_diff", *args, **kwargs)
