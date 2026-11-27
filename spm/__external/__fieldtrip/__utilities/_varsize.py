from spm._runtime import Runtime


def _varsize(*args, **kwargs):
    r"""
      VARSIZE returns the size of a variable in bytes. It can be used on any MATLAB  
        variable, including structures and cell arrays.  
         
        See also WHOS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/varsize.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("varsize", *args, **kwargs)
