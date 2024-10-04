from spm.__wrap__ import _Runtime


def spm_mvtpdf(*args, **kwargs):
  """  PDF of multivariate T-distribution  
    FORMAT [p] = spm_mvtpdf (x,mu,Lambda,v)  
     
    x      - ordinates [d x N]  
    mu     - mean [d x 1]  
    Lambda - precision matrix [d x d]  
    v      - degrees of freedom  
     
    p      - probability density  
     
    See J. Bernardo and A. Smith (2000)   
    Bayesian Theory, Wiley (page 435)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mvtpdf.m)
  """

  return _Runtime.call("spm_mvtpdf", *args, **kwargs)
