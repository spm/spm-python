from spm.__wrapper__ import Runtime


def _plgndr(*args, **kwargs):
  """  PLGNDR associated Legendre function  
     
    y = plgndr(n,k,x) computes the values of the associated Legendre functions  
    of degree N and order K  
     
    implemented as MEX file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/plgndr.m)
  """

  return Runtime.call("plgndr", *args, **kwargs)
