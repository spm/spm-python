from spm.__wrap__ import _Runtime


def spm_bgt_priors(*args, **kwargs):
  """  Prior moments for a basal ganglia circuit  
    FORMAT [pE,pC] = spm_bgt_priors  
    only contains priors for intrinsic parameters  
    priors for extrinsic parameters are defined in spm_cmc_priors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_bgt_priors.m)
  """

  return _Runtime.call("spm_bgt_priors", *args, **kwargs)
