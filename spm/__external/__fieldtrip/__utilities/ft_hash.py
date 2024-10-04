from spm.__wrap__ import _Runtime


def ft_hash(*args, **kwargs):
  """  FT_HASH computes a MD5 hash from a MATLAB variable or structure  
     
    It will first try a hashing algorithm implemented as a mex file.  
    If that fails, it falls back to a slower one that is based on Java.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_hash.m)
  """

  return _Runtime.call("ft_hash", *args, **kwargs)
