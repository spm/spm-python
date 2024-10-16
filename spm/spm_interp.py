from spm.__wrapper__ import Runtime


def spm_interp(*args, **kwargs):
  """  1 or 2-D array interpolation  
    FORMAT [x] = spm_interp(x,r)  
    x - array  
    r - interpolation rate  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_interp.m)
  """

  return Runtime.call("spm_interp", *args, **kwargs)
