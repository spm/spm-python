from spm.__wrap__ import _Runtime


def spm_lx_phase(*args, **kwargs):
  """  Observation function for phase-coupled oscillators  
    FORMAT [G] = spm_lx_phase(P,M)  
     
    G     Observations y = Gx  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_lx_phase.m)
  """

  return _Runtime.call("spm_lx_phase", *args, **kwargs)
