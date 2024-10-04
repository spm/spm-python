from spm.__wrap__ import _Runtime


def spm_gen_ind(*args, **kwargs):
  """  Generate a prediction of trial-specific induced activity  
    FORMAT [y] = spm_gen_ind(P,M,U)  
     
    P - parameters  
    M - neural-mass model structure  
    U - trial-specific effects  
     
    y - prediction  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gen_ind.m)
  """

  return _Runtime.call("spm_gen_ind", *args, **kwargs)
