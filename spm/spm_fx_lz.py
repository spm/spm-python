from spm.__wrap__ import _Runtime


def spm_fx_lz(*args, **kwargs):
  """  flow for Lorenz attractor  
    FORMAT [y] = spm_fx_lz(x,u,P)  
    x - state  
    u - input  
    P - parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_fx_lz.m)
  """

  return _Runtime.call("spm_fx_lz", *args, **kwargs)
