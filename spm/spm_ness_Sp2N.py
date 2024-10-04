from spm.__wrap__ import _Runtime


def spm_ness_Sp2N(*args, **kwargs):
  """  Convert polynomial potential parameters into a Gaussian density  
    FORMAT [m,C] = spm_ness_Sp2N(Sp,[n,K])  
   --------------------------------------------------------------------------  
    Sp - Polynomial coefficients or parameters of log density  
    n  - Dimensionality of state space  
    K  - Order of polynomial expansion (K = 3 corresponds to quadratic)  
     
    m  - (Gaussian) mean  
    C  - (Gaussian) covariance  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ness_Sp2N.m)
  """

  return _Runtime.call("spm_ness_Sp2N", *args, **kwargs)
