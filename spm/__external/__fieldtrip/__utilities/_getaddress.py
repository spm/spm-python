from spm.__wrap__ import _Runtime


def _getaddress(*args, **kwargs):
  """  GETADDRESS returns the IP address  
     
    Use as  
      address = getaddress();  
    or  
      address = getaddress(hostname);  
     
    See also GETUSERNAME, GETHOSTNAME  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/getaddress.m)
  """

  return _Runtime.call("getaddress", *args, **kwargs)
