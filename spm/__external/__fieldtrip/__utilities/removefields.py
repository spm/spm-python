from spm.__wrap__ import _Runtime


def removefields(*args, **kwargs):
  """  REMOVEFIELDS makes a selection of the fields in a structure  
     
    Use as  
      s = removefields(s, fields);  
     
    See also KEEPFIELDS, COPYFIELDS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/removefields.m)
  """

  return _Runtime.call("removefields", *args, **kwargs)
