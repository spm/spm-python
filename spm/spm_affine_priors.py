from spm.__wrapper__ import Runtime


def spm_affine_priors(*args, **kwargs):
  """  Distribution of the priors used in affine registration  
     
    The parameters for this distribution were derived empirically from 227  
    scans, that were matched to the ICBM space.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_affine_priors.m)
  """

  return Runtime.call("spm_affine_priors", *args, **kwargs)
