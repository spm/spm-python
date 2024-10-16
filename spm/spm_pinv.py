from spm.__wrapper__ import Runtime


def spm_pinv(*args, **kwargs):
  """  Pseudo-inverse for sparse matrices  
    FORMAT X = spm_pinv(A,TOL)  
     
    A   - matrix  
    TOL - Tolerance to force singular value decomposition  
    X   - generalised inverse  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_pinv.m)
  """

  return Runtime.call("spm_pinv", *args, **kwargs)
