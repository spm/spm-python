from spm.__wrapper__ import Runtime


def spm_immune_priors(*args, **kwargs):
  """  Default priors for immune model  
    FORMAT [P,C] = spm_immune_priors  
    P - Prior expectations  
    C - Prior covariances  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_priors.m)
  """

  return Runtime.call("spm_immune_priors", *args, **kwargs)
