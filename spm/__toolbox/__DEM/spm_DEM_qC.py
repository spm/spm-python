from spm.__wrapper__ import Runtime


def spm_DEM_qC(*args, **kwargs):
  """  returns the conditional precision over hidden states  
    FORMAT [qP] = spm_DEM_qC(M)  
     
    M  - recognition  model  
      M(1).x    = Conditional expectation of hidden states  
      M(1).v    = Conditional expectation of causal states  
     
    qP     - conditional precision, evaluated at M.x, M.v  
   __________________________________________________________________________  
     
    see spm_DEM and spm_ADEM for details.  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_qC.m)
  """

  return Runtime.call("spm_DEM_qC", *args, **kwargs)
