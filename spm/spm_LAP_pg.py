from spm.__wrap__ import _Runtime


def spm_LAP_pg(*args, **kwargs):
  """  Default precision function for LAP models (hidden states)  
    FORMAT p = spm_LAP_pg(x,v,h,M)  
     
    x  - hidden states  
    v  - causal states  
    h  - precision parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_LAP_pg.m)
  """

  return _Runtime.call("spm_LAP_pg", *args, **kwargs)
