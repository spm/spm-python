from spm.__wrapper__ import Runtime


def spm_eeg_inv_transform_points(*args, **kwargs):
  """  Apply homogeneous transformation to a set of 3D points  
    FORMAT new = spm_eeg_inv_transform_points(M, old)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_transform_points.m)
  """

  return Runtime.call("spm_eeg_inv_transform_points", *args, **kwargs)
