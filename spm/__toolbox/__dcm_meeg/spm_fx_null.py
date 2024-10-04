from spm.__wrap__ import _Runtime


def spm_fx_null(*args, **kwargs):
  """  State equations for null (Jacobian) model  
    FORMAT [f,J] = spm_fx_null(x,u,P,M)  
     
    x - hidden states  
    u - exogenous input  
    P - parameters  
    M - model  
     
    f - flow  
    J - Jacobian  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_null.m)
  """

  return _Runtime.call("spm_fx_null", *args, **kwargs)
