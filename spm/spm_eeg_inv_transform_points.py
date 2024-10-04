from spm.__wrap__ import _Runtime


def spm_eeg_inv_transform_points(*args, **kwargs):
  """  Apply homogeneous transformation to a set of 3D points  
    FORMAT new = spm_eeg_inv_transform_points(M, old)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_transform_points.m)
  """

  return _Runtime.call("spm_eeg_inv_transform_points", *args, **kwargs)
