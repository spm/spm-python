from spm.__wrapper__ import Runtime


def getpid(*args, **kwargs):
  """  GETPID returns the process identifier (PID) of the current Matlab  
    process.  
     
    Use as  
      num = getpid;  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/getpid.m)
  """

  return Runtime.call("getpid", *args, **kwargs)
