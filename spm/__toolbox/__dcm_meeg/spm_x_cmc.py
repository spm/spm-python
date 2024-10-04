from spm.__wrap__ import _Runtime


def spm_x_cmc(*args, **kwargs):
  """  Initial state of a canonical microcircuit model  
    FORMAT [x] = spm_x_cmc(P)  
    P - parameters  
     
    x        - x(0)  
   __________________________________________________________________________  
    David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
    neuronal dynamics. NeuroImage 20: 1743-1755  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_x_cmc.m)
  """

  return _Runtime.call("spm_x_cmc", *args, **kwargs)
