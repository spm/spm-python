from spm.__wrap__ import _Runtime


def spm_dcm_reduce(*args, **kwargs):
  """  Reduce the posterior of DCM given new priors (rE,rC)  
    FORMAT RCM = spm_dcm_reduce(DCM,rE,rC)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_reduce.m)
  """

  return _Runtime.call("spm_dcm_reduce", *args, **kwargs)
