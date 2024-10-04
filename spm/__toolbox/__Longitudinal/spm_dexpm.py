from spm.__wrap__ import _Runtime


def spm_dexpm(*args, **kwargs):
  """  Differentiate a matrix exponential  
    FORMAT [E,dE] = spm_dexpm(A,dA)  
    A  - Lie algebra  
    dA - basis function to differentiate with respect to  
     
    E  - expm(A)  
    dE - (expm(A+eps*dA)-expm(A-eps*dA))/(2*eps)  
     
    Note that the algorithm is a bit slow, and should perhaps be re-written  
    to use eg scaling and squaring (see Moler's dubious matrix exponentials  
    paper).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_dexpm.m)
  """

  return _Runtime.call("spm_dexpm", *args, **kwargs)
