from spm.__wrap__ import _Runtime


def _size_equal(*args, **kwargs):
  """  returns true if all input arguments are equal to each other  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/private/size_equal.m)
  """

  return _Runtime.call("size_equal", *args, **kwargs)
