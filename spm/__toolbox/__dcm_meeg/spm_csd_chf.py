from spm.__wrapper__ import Runtime


def spm_csd_chf(*args, **kwargs):
  """  Characteristic (expected) frequency of a NMM  
    FORMAT [G,w] = spm_csd_chf(P,M,U)  
     
    P - parameters  
    M - neural mass model structure  
    U - trial-specific effects  
     
    m - expected frequency  
    v - dispersion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_csd_chf.m)
  """

  return Runtime.call("spm_csd_chf", *args, **kwargs)
