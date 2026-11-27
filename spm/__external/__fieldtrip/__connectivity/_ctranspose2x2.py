from spm._runtime import Runtime


def _ctranspose2x2(*args, **kwargs):
    r"""
      compute ctranspose of multiple 2x2 matrices, input is 2x2xN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/ctranspose2x2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ctranspose2x2", *args, **kwargs)
