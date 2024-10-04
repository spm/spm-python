from spm.__wrap__ import _Runtime


def spm_affine_priors(*args, **kwargs):
  """  Distribution of the priors used in affine registration  
     
    The parameters for this distribution were derived empirically from 227  
    scans, that were matched to the ICBM space.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_affine_priors.m)
  """

  return _Runtime.call("spm_affine_priors", *args, **kwargs)
