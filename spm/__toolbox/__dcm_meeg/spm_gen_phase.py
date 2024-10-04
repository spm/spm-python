from spm.__wrap__ import _Runtime


def spm_gen_phase(*args, **kwargs):
  """  Generate state activities for trial-specific phase-coupled activity  
    FORMAT [x] = spm_gen_phase(P,M,U)  
     
    P - parameters  
    M - model structure  
    U - trial-specific effects  
     
    x - states  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gen_phase.m)
  """

  return _Runtime.call("spm_gen_phase", *args, **kwargs)
