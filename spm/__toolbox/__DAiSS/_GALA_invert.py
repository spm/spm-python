from spm.__wrapper__ import Runtime


def _GALA_invert(*args, **kwargs):
  """GALA_invert is a function.  
      [J, S] = GALA_invert(BF, tS)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_invert.m)
  """

  return Runtime.call("GALA_invert", *args, **kwargs)
