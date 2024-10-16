from spm.__wrapper__ import Runtime


def spm_gx_SHC(*args, **kwargs):
  """  maps to state of a SCH to a 2-D position in the world  
    FORMAT [g] = spm_gx_SHC(x,v,P)  
     
    x    - vector of hidden sates  
    P.g  - state-space location associated with each hidden states  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_SHC.m)
  """

  return Runtime.call("spm_gx_SHC", *args, **kwargs)
