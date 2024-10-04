from spm.__wrap__ import _Runtime


def spm_ness_m2S(*args, **kwargs):
  """  Conditional moments of a Gaussian density (polynomial parameterisation)  
    FORMAT [p0,X,F,f,NESS] = spm_ness_hd(M,x)  
   --------------------------------------------------------------------------  
    m  - (Conditional) mean  
    C  - (Conditional) covariance  
     
    Sp - Polynomial coefficients or parameters of log density  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ness_m2S.m)
  """

  return _Runtime.call("spm_ness_m2S", *args, **kwargs)
