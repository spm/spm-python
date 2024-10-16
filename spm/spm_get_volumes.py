from spm.__wrapper__ import Runtime


def spm_get_volumes(*args, **kwargs):
  """  Compute total volumes from tissue segmentations  
    FORMAT gl = spm_get_volumes(P)  
    P  - a matrix of image filenames  
    gl - a vector of volumes (in litres)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_get_volumes.m)
  """

  return Runtime.call("spm_get_volumes", *args, **kwargs)
