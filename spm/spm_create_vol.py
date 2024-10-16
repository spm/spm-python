from spm.__wrapper__ import Runtime


def spm_create_vol(*args, **kwargs):
  """  Create a NIfTI image volume  
    FORMAT V = spm_create_vol(V)  
    V        - image volume information (see spm_vol.m)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_create_vol.m)
  """

  return Runtime.call("spm_create_vol", *args, **kwargs)
