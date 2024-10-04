from spm.__wrap__ import _Runtime


def spm_TVdenoise2(*args, **kwargs):
  """   
    FORMAT y = spm_TVdenoise2(x, lambda, nit, y)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise2.m)
  """

  return _Runtime.call("spm_TVdenoise2", *args, **kwargs)
