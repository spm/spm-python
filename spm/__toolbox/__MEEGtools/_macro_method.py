from spm._runtime import Runtime


def _macro_method(*args, **kwargs):
    r"""
      MACRO_METHOD: Script to insert at the beginning of all the brainstorm class functions  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/private/macro_method.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("macro_method", *args, **kwargs)
