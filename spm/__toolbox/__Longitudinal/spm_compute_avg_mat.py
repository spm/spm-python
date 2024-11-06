from spm.__wrapper__ import Runtime


def spm_compute_avg_mat(*args, **kwargs):
    """
      Compute an average voxel-to-world mapping and suitable dimensions  
        FORMAT [M_avg,d] = spm_compute_avg_mat(Mat0,dims)  
        Mat0  - array of matrices (4x4xN)  
        dims  - image dimensions (Nx3)  
        M_avg - voxel-to-world mapping  
        d     - dimensions for average image  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_compute_avg_mat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_compute_avg_mat", *args, **kwargs)
