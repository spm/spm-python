from spm.__wrap__ import _Runtime


def spm_trace(*args, **kwargs):
  """  Fast trace for large matrices: C = spm_trace(A,B) = trace(A*B)  
    FORMAT [C] = spm_trace(A,B)  
     
    C = spm_trace(A,B) = trace(A*B) = sum(sum(A'.*B));  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_trace.m)
  """

  return _Runtime.call("spm_trace", *args, **kwargs)
