from spm.__wrapper__ import Runtime


def copyfields(*args, **kwargs):
  """  COPYFIELDS copies a selection of the fields from one structure to another  
     
    Use as  
      b = copyfields(a, b, fields);  
    which copies the specified fields over from structure a to structure b. Fields that  
    are specified but not present will be silently ignored.  
     
    See also KEEPFIELDS, REMOVEFIELDS, RENAMEFIELDS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/copyfields.m)
  """

  return Runtime.call("copyfields", *args, **kwargs)
