from spm.__wrap__ import _Runtime


def spm_detrend(*args, **kwargs):
  """  Polynomial detrending over columns  
    FORMAT y = spm_detrend(x,p)  
    x   - data matrix  
    p   - order of polynomial [default: 0]  
      
    y   - detrended data matrix  
   __________________________________________________________________________  
     
    spm_detrend removes linear and nonlinear trends from column-wise data  
    matrices.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_detrend.m)
  """

  return _Runtime.call("spm_detrend", *args, **kwargs)
