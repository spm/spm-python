from spm.__wrap__ import _Runtime


def spm_get_space(*args, **kwargs):
  """  Get/set the voxel-to-world mapping of an image  
    FORMAT M = spm_get_space(P)  
               spm_get_space(P,M)  
    P - image filename  
    M - voxel-to-world mapping  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_get_space.m)
  """

  return _Runtime.call("spm_get_space", *args, **kwargs)
