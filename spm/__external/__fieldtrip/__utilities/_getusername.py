from spm.__wrap__ import _Runtime


def _getusername(*args, **kwargs):
  """  GETUSERNAME  
     
    Use as  
      str = getusername();  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getusername.m)
  """

  return _Runtime.call("getusername", *args, **kwargs)
