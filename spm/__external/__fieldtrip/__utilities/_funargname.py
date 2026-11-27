from spm._runtime import Runtime


def _funargname(*args, **kwargs):
    r"""
      FUNARGNAME returns the input and output arguments of the function  
        by parsing the m-file  
         
        Use as  
           [input, output] = funargname(fname)  
        where the input and output function arguments will be returned  
        as cell-arrays containing strings.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/funargname.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("funargname", *args, **kwargs)
