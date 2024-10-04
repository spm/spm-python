from spm.__wrap__ import _Runtime


def spm_fileparts(*args, **kwargs):
  """  Like fileparts, but separates off a comma separated list at the end  
    FORMAT [pth,nam,ext,num] = spm_fileparts(fname)  
    fname  - original filename  
     
    pth    - path  
    nam    - filename  
    ext    - extension  
    num    - comma separated list of values  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_fileparts.m)
  """

  return _Runtime.call("spm_fileparts", *args, **kwargs)
