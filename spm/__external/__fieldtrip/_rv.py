from spm._runtime import Runtime


def _rv(*args, **kwargs):
    r"""
      RV returns the relative residual variance between measured and simulated data  
         
        rv = rv(measured, simulated)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/rv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("rv", *args, **kwargs)
