from mpython import Runtime


def spm_cov2corr(*args, **kwargs):
    """
      Correlation matrix given the covariance matrix
        FORMAT R = spm_cov2corr(C)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cov2corr.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cov2corr", *args, **kwargs)
