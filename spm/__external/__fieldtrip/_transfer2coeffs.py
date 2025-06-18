from mpython import Runtime


def _transfer2coeffs(*args, **kwargs):
    """
      TRANSFER2COEFFS converts a spectral transfer matrix into the time domain
        equivalent multivariate autoregressive coefficients up to a specified
        lag, starting from lag 1.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/transfer2coeffs.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("transfer2coeffs", *args, **kwargs)
