from spm.__wrap__ import _Runtime


def _GALA_invert(*args, **kwargs):
  """GALA_invert is a function.  
      [J, S] = GALA_invert(BF, tS)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_invert.m)
  """

  return _Runtime.call("GALA_invert", *args, **kwargs)
