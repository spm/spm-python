from spm._runtime import Runtime


def _ismatch(*args, **kwargs):
    r"""
      ISMATCH returns true if x is a member of array y, regardless of the class  
        of x and y, if y is a string, or a cell-array of strings, it can contain  
        the wildcard '*'  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/ismatch.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ismatch", *args, **kwargs)
