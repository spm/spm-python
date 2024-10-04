from spm.__wrap__ import _Runtime


def boxcar(*args, **kwargs):
  """  BOXCAR returns a boxcar taper  
     
    Use as  
      w = boxcar(n)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/boxcar.m)
  """

  return _Runtime.call("boxcar", *args, **kwargs)
