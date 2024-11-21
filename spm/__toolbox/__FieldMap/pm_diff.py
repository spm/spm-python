from spm.__wrapper__ import Runtime


def pm_diff(*args, **kwargs):
    """
      Calculate derivative in one direction of volume (matrix or memory mapped)  
        FORMAT D = pm_diff(V,dir)  
        V    - 3D array, or filestruct returned from spm_vol  
        dir  - direction (1, 2 or 3 for x, y or z respectively)  
         
        D    - 3D array of derivatives  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_diff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_diff", *args, **kwargs)
