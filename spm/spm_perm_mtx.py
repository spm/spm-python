from spm.__wrap__ import _Runtime


def spm_perm_mtx(*args, **kwargs):
  """  Return a matrix of indices permuted over n  
    FORMAT [K] = spm_perm_mtx(n)  
       n   - (scalar) number of indices  
       K   - (2^n x n) permutation matrix  
    or  
       n   - (vector) indices  
       K   - (length(n)! x n) permutation matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_perm_mtx.m)
  """

  return _Runtime.call("spm_perm_mtx", *args, **kwargs)
