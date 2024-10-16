from spm.__wrapper__ import Runtime


def renamefields(*args, **kwargs):
  """  RENAMEFIELDS renames a selection of the fields in a structure  
     
    Use as  
      b = renamefields(a, old, new)  
    which renames the fields with the old name to the new name. Fields that  
    are specified but not present will be silently ignored.  
     
    See also COPYFIELDS, KEEPFIELDS, REMOVEFIELDS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/renamefields.m)
  """

  return Runtime.call("renamefields", *args, **kwargs)
