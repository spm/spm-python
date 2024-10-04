from spm.__wrap__ import _Runtime


def spm_compact_svd(*args, **kwargs):
  """  Local SVD with compact support for large matrices  
    FORMAT U = spm_compact_svd(Y,xyz,nu)  
    Y     - matrix  
    xyz   - location  
    nu    - number of vectors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_compact_svd.m)
  """

  return _Runtime.call("spm_compact_svd", *args, **kwargs)
