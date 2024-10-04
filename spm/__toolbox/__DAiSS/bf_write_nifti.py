from spm.__wrap__ import _Runtime


def bf_write_nifti(*args, **kwargs):
  """  Writes out nifti images of beamformer results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_nifti.m)
  """

  return _Runtime.call("bf_write_nifti", *args, **kwargs)
