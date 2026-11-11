from spm._runtime import Runtime


def renamefields(*args, **kwargs):
    r"""
      RENAMEFIELDS renames a selection of the fields in a structure  
         
        Use as  
          b = renamefields(a, old, new)  
        which renames the fields with the old name to the new name. Fields that  
        are specified but not present will be silently ignored.  
         
        See also COPYFIELDS, KEEPFIELDS, REMOVEFIELDS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/renamefields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("renamefields", *args, **kwargs)
