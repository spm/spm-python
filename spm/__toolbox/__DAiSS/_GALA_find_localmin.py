from spm.__wrap__ import _Runtime


def _GALA_find_localmin(*args, **kwargs):
  """GALA_find_localmin is a function.  
      regions = GALA_find_localmin(lJcov, Nl, Nd, A, thresh)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_find_localmin.m)
  """

  return _Runtime.call("GALA_find_localmin", *args, **kwargs)
