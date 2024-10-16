from spm.__wrapper__ import Runtime


def _mplgndr(*args, **kwargs):
  """  MPLGNDR associated Legendre functions  
     
    y = mplgndr(n,k,x) computes the values of the associated Legendre  
    functions of order K up to degree N.  
      
    The input x can be a matrix, and the result is of size numel(x) by N+1.  
    The i-th column is the associated Legendre function of order K and  
    degree i-1.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mplgndr.m)
  """

  return Runtime.call("mplgndr", *args, **kwargs)
