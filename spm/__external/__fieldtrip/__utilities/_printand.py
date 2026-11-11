from spm._runtime import Runtime


def _printand(*args, **kwargs):
    r"""
      PRINTAND prints a single or multiple strings as "x1, x2, x3 and x4". If there is  
        only one string, that string is returned without additional formatting.  
         
        See also PRINTOR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/printand.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("printand", *args, **kwargs)
