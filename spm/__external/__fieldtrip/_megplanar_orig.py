from spm.__wrap__ import _Runtime


def _megplanar_orig(*args, **kwargs):
  """  This is the original method from Ole.  It has a different way of  
    making the coordinate transformation that I do not fully understand.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_orig.m)
  """

  return _Runtime.call("megplanar_orig", *args, **kwargs)
