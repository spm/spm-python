from spm.__wrapper__ import Runtime


def _pinvNx2(*args, **kwargs):
    """
      PINVNX2 computes a pseudo-inverse of the M slices of an MxNx2 real-valued matrix.  
        Output has dimensionality Mx2xN. This implementation is generally faster  
        than calling pinv in a for-loop, once M > 2  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/pinvNx2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pinvNx2", *args, **kwargs)
