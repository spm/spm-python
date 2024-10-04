from spm.__wrap__ import _Runtime


def range(*args, **kwargs):
  """  RANGE computes the range (i.e. difference between min and max) for a vector  
    or an N-dimensional array.   
     
    Use as  
      r = range(x)  
    or you can also specify the dimension along which to look by  
      r = range(x, dim)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/range.m)
  """

  return _Runtime.call("range", *args, **kwargs)
