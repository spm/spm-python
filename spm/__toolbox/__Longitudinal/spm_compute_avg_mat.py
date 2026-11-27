from spm._runtime import Runtime


def spm_compute_avg_mat(*args, **kwargs):
    r"""
      Compute an average voxel-to-world mapping and suitable dimensions  
        FORMAT [M_avg,d] = spm_compute_avg_mat(Mat0,dims)  
        Mat0  - array of matrices (4x4xN)  
        dims  - image dimensions (Nx3)  
        M_avg - voxel-to-world mapping  
        d     - dimensions for average image  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Longitudinal/spm_compute_avg_mat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_compute_avg_mat", *args, **kwargs)
