from spm.__wrapper__ import Runtime


def spm_get_data(*args, **kwargs):
    """
      Get data from image files at specified locations  
        FORMAT [Y] = spm_get_data(V,XYZ,check)  
         
        V          - [1 x n] struct array of file handles (or filename matrix)  
        XYZ        - [3 x m] or [4 x m] location matrix {voxel}  
        check      - check validity of input parameters [default: true]  
         
        Y          - [n x m] double values  
         
        See also spm_sample_vol  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_data", *args, **kwargs)
