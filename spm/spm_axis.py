from spm._runtime import Runtime


def spm_axis(*args, **kwargs):
    r"""
      AXIS  Control axis scaling and appearance.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_axis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_axis", *args, **kwargs)
