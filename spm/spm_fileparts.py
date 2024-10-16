from spm.__wrapper__ import Runtime


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

  return Runtime.call("spm_fileparts", *args, **kwargs)
