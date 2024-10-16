from spm.__wrapper__ import Runtime


def spm_slice2vol(*args, **kwargs):
  """  Slice-to-volume alignment job  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol.m)
  """

  return Runtime.call("spm_slice2vol", *args, **kwargs)
