from spm._runtime import Runtime


def _transfer2coeffs(*args, **kwargs):
    r"""
      TRANSFER2COEFFS converts a spectral transfer matrix into the time domain  
        equivalent multivariate autoregressive coefficients up to a specified  
        lag, starting from lag 1.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/transfer2coeffs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("transfer2coeffs", *args, **kwargs)
