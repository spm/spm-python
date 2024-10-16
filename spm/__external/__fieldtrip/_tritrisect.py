from spm.__wrapper__ import Runtime


def _tritrisect(*args, **kwargs):
  """  TRITRISECT computes the intersection line of a triangle with a plane  
    spanned by three vertices v1, v2 and v3.  
     
    [l1, l2] = tritrisect(v1, v2, v3, t1, t2, t3)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/tritrisect.m)
  """

  return Runtime.call("tritrisect", *args, **kwargs)
