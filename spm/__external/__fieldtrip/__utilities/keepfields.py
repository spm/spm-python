from spm.__wrapper__ import Runtime


def keepfields(*args, **kwargs):
  """  KEEPFIELDS makes a selection of the fields in a structure  
     
    Use as  
      s = keepfields(s, fields);  
     
    See also REMOVEFIELDS, COPYFIELDS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/keepfields.m)
  """

  return Runtime.call("keepfields", *args, **kwargs)
