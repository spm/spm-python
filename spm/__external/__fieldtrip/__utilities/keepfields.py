from spm._runtime import Runtime


def keepfields(*args, **kwargs):
    r"""
      KEEPFIELDS makes a selection of the fields in a structure  
         
        Use as  
          s = keepfields(s, fields);  
         
        See also REMOVEFIELDS, COPYFIELDS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/keepfields.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keepfields", *args, **kwargs)
