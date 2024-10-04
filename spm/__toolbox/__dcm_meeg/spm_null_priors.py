from spm.__wrap__ import _Runtime


def spm_null_priors(*args, **kwargs):
  """  Prior moments for null (Jacobian) model  
    FORMAT [pE,pC] = spm_null_priors(A,B,C)  
     
    A{1},B{m},C  - binary constraints on extrinsic connections  
     
    pE - prior expectation  
    pC - prior covariance  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_null_priors.m)
  """

  return _Runtime.call("spm_null_priors", *args, **kwargs)
