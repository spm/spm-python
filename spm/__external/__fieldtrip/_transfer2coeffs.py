from spm.__wrapper__ import Runtime


def _transfer2coeffs(*args, **kwargs):
    """
      TRANSFER2COEFFS converts a spectral transfer matrix into the time domain  
        equivalent multivariate autoregressive coefficients up to a specified  
        lag, starting from lag 1.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/transfer2coeffs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("transfer2coeffs", *args, **kwargs)
