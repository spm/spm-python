from spm.__wrap__ import _Runtime


def spm_ssm2s(*args, **kwargs):
  """  Convert state-space (M) representation to eigenspectrum  
    FORMAT [s,u] = spm_ssm2s(P,M,TOL)  
     
    P    - model parameters  
    M    - model (with flow M.f and expansion point M.x and M.u)  
    TOL  - optional upper bound for  principality exponent  (default -4)  
     
    S    - (sorted) eigenspectrum or Lyapunov exponents  
    V    - associated eigenvectors  
     
    csd  - cross spectral density  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ssm2s.m)
  """

  return _Runtime.call("spm_ssm2s", *args, **kwargs)
