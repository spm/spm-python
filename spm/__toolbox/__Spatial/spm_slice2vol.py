from spm.__wrap__ import _Runtime


def spm_slice2vol(*args, **kwargs):
  """  Slice-to-volume alignment job  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol.m)
  """

  return _Runtime.call("spm_slice2vol", *args, **kwargs)
