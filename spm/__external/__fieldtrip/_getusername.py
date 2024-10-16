from spm.__wrapper__ import Runtime


def _getusername(*args, **kwargs):
  """  GETUSERNAME  
     
    Use as  
      str = getusername();  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/getusername.m)
  """

  return Runtime.call("getusername", *args, **kwargs)
