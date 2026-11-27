from spm._runtime import Runtime


def _inv2x2(*args, **kwargs):
    r"""
      INV2X2 computes inverse of matrix x, using explicit analytic definition  
        if size(x,1) < 4, otherwise use MATLAB inv-function  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/inv2x2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("inv2x2", *args, **kwargs)
