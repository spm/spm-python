from spm.__wrapper__ import Runtime


def spm_hist_smooth(*args, **kwargs):
  """  Histogram smoothing (graph Laplacian)  
    FORMAT x = spm_hist_smooth(x,s)  
    x   - data vector  
    s   - smoothing  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hist_smooth.m)
  """

  return Runtime.call("spm_hist_smooth", *args, **kwargs)
