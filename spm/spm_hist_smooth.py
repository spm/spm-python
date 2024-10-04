from spm.__wrap__ import _Runtime


def spm_hist_smooth(*args, **kwargs):
  """  Histogram smoothing (graph Laplacian)  
    FORMAT x = spm_hist_smooth(x,s)  
    x   - data vector  
    s   - smoothing  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hist_smooth.m)
  """

  return _Runtime.call("spm_hist_smooth", *args, **kwargs)
