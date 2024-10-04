from spm.__wrap__ import _Runtime


def _isrealmat(*args, **kwargs):
  """  ISREALMAT returns true for a real matrix  
     
    Use as  
      status = isrealmat(x)  
     
    See also ISNUMERIC, ISREAL, ISVECTOR, ISREALVEC  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/isrealmat.m)
  """

  return _Runtime.call("isrealmat", *args, **kwargs)
