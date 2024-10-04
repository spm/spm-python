from spm.__wrap__ import _Runtime


def _megplanar_sincos(*args, **kwargs):
  """  This attempts to re-implements Ole's method, exept that the definition of the  
    horizontal and vertical direction is different.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/megplanar_sincos.m)
  """

  return _Runtime.call("megplanar_sincos", *args, **kwargs)
