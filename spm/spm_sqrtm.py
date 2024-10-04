from spm.__wrap__ import _Runtime


def spm_sqrtm(*args, **kwargs):
  """  Matrix square root for sparse symmetric positive semi-definite matrices  
    FORMAT [K] = spm_sqrtm(V)  
     
    This routine covers and extends sqrtm functionality by using a  
    computationally expedient approximation that can handle sparse symmetric  
    positive semi-definite matrices.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_sqrtm.m)
  """

  return _Runtime.call("spm_sqrtm", *args, **kwargs)
