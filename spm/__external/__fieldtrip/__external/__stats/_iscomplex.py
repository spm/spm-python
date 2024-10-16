from spm.__wrapper__ import Runtime


def _iscomplex(*args, **kwargs):
  """iscomplex is a function.  
      a = iscomplex(X)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/private/iscomplex.m)
  """

  return Runtime.call("iscomplex", *args, **kwargs)
