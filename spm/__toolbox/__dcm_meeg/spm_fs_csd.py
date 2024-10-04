from spm.__wrap__ import _Runtime


def spm_fs_csd(*args, **kwargs):
  """  Spectral feature selection for a CSD DCM  
    FORMAT [y] = spm_fs_csd(y,M)  
    y      - CSD  
    M      - model structure  
   __________________________________________________________________________  
     
    David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
    neuronal dynamics. NeuroImage 20: 1743-1755  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fs_csd.m)
  """

  return _Runtime.call("spm_fs_csd", *args, **kwargs)
