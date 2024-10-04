from spm.__wrap__ import _Runtime


def spm_Q_perm(*args, **kwargs):
  """  Return a cell of permutation indices for separating matrices  
    FORMAT p = spm_Q_perm(Q)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_Q_perm.m)
  """

  return _Runtime.call("spm_Q_perm", *args, **kwargs)
