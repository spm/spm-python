from spm.__wrap__ import _Runtime


def getpid(*args, **kwargs):
  """  GETPID returns the process identifier (PID) of the current Matlab  
    process.  
     
    Use as  
      num = getpid;  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/getpid.m)
  """

  return _Runtime.call("getpid", *args, **kwargs)
