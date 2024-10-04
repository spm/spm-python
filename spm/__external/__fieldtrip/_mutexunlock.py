from spm.__wrap__ import _Runtime


def _mutexunlock(*args, **kwargs):
  """  MUTEXUNLOCK removes a lockfile  
     
    Use as  
      mutexunlock(lockfile)  
     
    See also MUTEXLOCK and http://en.wikipedia.org/wiki/Mutual_exclusion  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mutexunlock.m)
  """

  return _Runtime.call("mutexunlock", *args, **kwargs, nargout=0)
