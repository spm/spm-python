from spm.__wrapper__ import Runtime


def spm_Q_perm(*args, **kwargs):
  """  Return a cell of permutation indices for separating matrices  
    FORMAT p = spm_Q_perm(Q)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_Q_perm.m)
  """

  return Runtime.call("spm_Q_perm", *args, **kwargs)
