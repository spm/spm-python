from spm.__wrapper__ import Runtime


def spm_LAP_ph(*args, **kwargs):
  """  Default precision function for LAP models (causal states)  
    FORMAT p = spm_LAP_ph(x,v,h,M)  
     
    x  - hidden states  
    v  - causal states  
    h  - precision parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_LAP_ph.m)
  """

  return Runtime.call("spm_LAP_ph", *args, **kwargs)
