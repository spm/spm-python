from spm._runtime import Runtime


def copyfields(*args, **kwargs):
    r"""
      COPYFIELDS copies a selection of the fields from one structure to another  
         
        Use as  
          b = copyfields(a, b, fields);  
        which copies the specified fields over from structure a to structure b. Fields that  
        are specified but not present will be silently ignored.  
         
        See also KEEPFIELDS, REMOVEFIELDS, RENAMEFIELDS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/copyfields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("copyfields", *args, **kwargs)
