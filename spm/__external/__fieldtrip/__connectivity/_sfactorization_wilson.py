from spm.__wrap__ import _Runtime


def _sfactorization_wilson(*args, **kwargs):
  """  SFACTORIZATION_WILSON performs multivariate non-parametric spectral factorization on  
    cross-spectra, based on Wilson's algorithm.  
     
    Usage  : [H, Z, S, psi] = sfactorization_wilson(S,freq);  
     
    Inputs : S (1-sided, 3D-spectral matrix in the form of Channel x Channel x frequency)  
           : freq (a vector of frequencies) at which S is given.  
     
    Outputs: H (transfer function)  
           : Z (noise covariance)  
           : psi (left spectral factor)  
     
    This function is an implemention of Wilson's algorithm (Eq. 3.1)  
    for spectral matrix factorization  
     
    Ref: G.T. Wilson,"The Factorization of Matricial Spectral Densities,"  
    SIAM J. Appl. Math.23,420-426(1972).  
    Written by M. Dhamala & G. Rangarajan, UF, Aug 3-4, 2006.  
    Email addresses: mdhamala@bme.ufl.edu, rangaraj@math.iisc.ernet.in  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/sfactorization_wilson.m)
  """

  return _Runtime.call("sfactorization_wilson", *args, **kwargs)
