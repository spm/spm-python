from spm._runtime import Runtime


def _det3x3(*args, **kwargs):
    r"""
      DET3X3 computes determinant of matrix x, using explicit analytic definition  
        if size(x) = [3 3 K M]  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/det3x3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("det3x3", *args, **kwargs)
