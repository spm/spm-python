from spm.__wrapper__ import Runtime


def renamefields(*args, **kwargs):
    """
      RENAMEFIELDS renames a selection of the fields in a structure  
         
        Use as  
          b = renamefields(a, old, new)  
        which renames the fields with the old name to the new name. Fields that  
        are specified but not present will be silently ignored.  
         
        See also COPYFIELDS, KEEPFIELDS, REMOVEFIELDS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/renamefields.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("renamefields", *args, **kwargs)
