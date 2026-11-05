from spm._runtime import Runtime


def _iscomplex(*args, **kwargs):
    r"""
    iscomplex is a function.  
          a = iscomplex(X)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/private/iscomplex.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("iscomplex", *args, **kwargs)
