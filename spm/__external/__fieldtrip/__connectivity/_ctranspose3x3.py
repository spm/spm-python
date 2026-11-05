from spm._runtime import Runtime


def _ctranspose3x3(*args, **kwargs):
    r"""
      compute ctranspose of multiple 3x3 matrices, input is 3x3xN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/ctranspose3x3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ctranspose3x3", *args, **kwargs)
