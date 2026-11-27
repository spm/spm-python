from spm._runtime import Runtime


def _reproducescript(*args, **kwargs):
    r"""
      This is a helper function to create a script that reproduces the analysis. It  
        appends the configuration and the function call to a MATLAB script.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/reproducescript.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("reproducescript", *args, **kwargs, nargout=0)
