from spm.__wrap__ import _Runtime


def spm_fp_display_nullclines(*args, **kwargs):
  """  Nullcline plot of flow and sample trajectory  
    FORMAT spm_fp_display_nullclines(M,x)  
     
    M   - model specifying flow; M(1).f;  
    x   - cell array of domain or support  
     
    f   - derivative of x(2)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_fp_display_nullclines.m)
  """

  return _Runtime.call("spm_fp_display_nullclines", *args, **kwargs)
