from spm.__wrap__ import _Runtime


def spm_compute_avg_mat(*args, **kwargs):
  """  Compute an average voxel-to-world mapping and suitable dimensions  
    FORMAT [M_avg,d] = spm_compute_avg_mat(Mat0,dims)  
    Mat0  - array of matrices (4x4xN)  
    dims  - image dimensions (Nx3)  
    M_avg - voxel-to-world mapping  
    d     - dimensions for average image  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_compute_avg_mat.m)
  """

  return _Runtime.call("spm_compute_avg_mat", *args, **kwargs)
