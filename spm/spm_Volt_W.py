from spm.__wrap__ import _Runtime


def spm_Volt_W(*args, **kwargs):
  """  Return basis functions used for Volterra expansion  
    FORMAT [W] = spm_Volt_W(u)  
    u  - times {seconds}  
    W  - basis functions (mixture of Gammas)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_Volt_W.m)
  """

  return _Runtime.call("spm_Volt_W", *args, **kwargs)
