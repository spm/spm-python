from spm.__wrap__ import _Runtime


def plgndr(*args, **kwargs):
  """  PLGNDR associated Legendre function  
     
    y = plgndr(n,k,x) computes the values of the associated Legendre functions  
    of degree N and order K  
     
    implemented as MEX file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/plgndr.m)
  """

  return _Runtime.call("plgndr", *args, **kwargs)
