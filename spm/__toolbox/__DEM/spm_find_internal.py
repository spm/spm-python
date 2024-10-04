from spm.__wrap__ import _Runtime


def spm_find_internal(*args, **kwargs):
  """  FORMAT nj = spm_find_internal(z,J)  
    finds indices of internal states (that do not contribute to slow modes)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_find_internal.m)
  """

  return _Runtime.call("spm_find_internal", *args, **kwargs)
