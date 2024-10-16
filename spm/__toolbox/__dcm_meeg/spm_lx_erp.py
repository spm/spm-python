from spm.__wrapper__ import Runtime


def spm_lx_erp(*args, **kwargs):
  """  Observer matrix for a neural mass model: y = G*x  
    FORMAT [G] = spm_lx_erp(P,dipfit)  
    FORMAT [G] = spm_lx_erp(P,M)  
     
    M.dipfit - spatial model specification  
     
    G        - where y = L*x; G = dy/dx  
    x        - state vector  
   __________________________________________________________________________  
     
    David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
    neuronal dynamics. NeuroImage 20: 1743-1755  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_lx_erp.m)
  """

  return Runtime.call("spm_lx_erp", *args, **kwargs)
