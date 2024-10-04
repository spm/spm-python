from spm.__wrap__ import _Runtime


def spm_Welcome(*args, **kwargs):
  """  Open SPM's welcome splash screen  
    FORMAT F = spm_Welcome  
    F        - welcome figure handle  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_Welcome.m)
  """

  return _Runtime.call("spm_Welcome", *args, **kwargs)
