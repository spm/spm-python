from spm._runtime import Runtime


def removefields(*args, **kwargs):
    r"""
      REMOVEFIELDS makes a selection of the fields in a structure  
         
        Use as  
          s = removefields(s, fields);  
         
        See also KEEPFIELDS, COPYFIELDS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/removefields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("removefields", *args, **kwargs)
