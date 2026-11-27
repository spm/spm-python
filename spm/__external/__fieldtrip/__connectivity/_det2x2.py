from spm._runtime import Runtime


def _det2x2(*args, **kwargs):
    r"""
      DET2X2 computes determinant of matrix x, using explicit analytic definition  
        if size(x,1) < 4, otherwise use MATLAB det-function  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/det2x2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("det2x2", *args, **kwargs)
