from spm.__wrapper__ import Runtime


def _isrealvec(*args, **kwargs):
  """  ISREALVEC returns true for a real row or column vector  
     
    Use as  
      status = isrealvec(x)  
     
    See also ISNUMERIC, ISREAL, ISVECTOR, ISREALMAT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/isrealvec.m)
  """

  return Runtime.call("isrealvec", *args, **kwargs)
