from spm.__wrap__ import _Runtime


def spm_load_float(*args, **kwargs):
  """  Load a volume into a floating point array  
    FORMAT dat = spm_load_float(V)  
    V   - handle from spm_vol  
    dat - a 3D floating point array  
   _______________________________________________________________________  
    Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_load_float.m)
  """

  return _Runtime.call("spm_load_float", *args, **kwargs)
