from spm.__wrap__ import _Runtime


def _gethostname(*args, **kwargs):
  """  HOSTNAME returns the hostname of this computer  
     
    Use as  
      str = hostname;  
     
    See also GETUSERNAME, GETADDRESS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/gethostname.m)
  """

  return _Runtime.call("gethostname", *args, **kwargs)
