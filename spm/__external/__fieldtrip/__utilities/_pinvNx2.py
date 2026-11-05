from spm._runtime import Runtime


def _pinvNx2(*args, **kwargs):
    r"""
      PINVNX2 computes a pseudo-inverse of the M slices of an MxNx2 real-valued matrix.  
        Output has dimensionality Mx2xN. This implementation is generally faster  
        than calling pinv in a for-loop, once M > 2  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/pinvNx2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("pinvNx2", *args, **kwargs)
