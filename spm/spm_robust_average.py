from spm.__wrap__ import _Runtime


def spm_robust_average(*args, **kwargs):
  """  Apply robust averaging routine to X sets  
    FORMAT [Y,W] = spm_robust_averaget(X, dim, ks)  
    X      - data matrix to be averaged  
    dim    - the dimension along which the function will work  
    ks     - offset of the weighting function (default: 3)  
     
    W      - estimated weights  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_robust_average.m)
  """

  return _Runtime.call("spm_robust_average", *args, **kwargs)
