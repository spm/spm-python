from spm.__wrapper__ import Runtime


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

  return Runtime.call("spm_fx_null", *args, **kwargs)
