from spm.__wrap__ import _Runtime


def spm_ness_flows(*args, **kwargs):
  """  Nonequilibrium steady-state under a Helmholtz decomposition  
    FORMAT spm_ness_flows(M,x)  
   --------------------------------------------------------------------------  
    M   - model specification structure  
    Required fields:  
       M.X  - sample points  
       M.W  - (n x n) - precision matrix of random fluctuations  
       M.K  - order of polynomial expansion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ness_flows.m)
  """

  return _Runtime.call("spm_ness_flows", *args, **kwargs, nargout=0)
