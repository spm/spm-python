from mpython import Runtime


def bf_features_csd(*args, **kwargs):
    """
      Compute cross-spectral density matrix for DICS
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_csd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features_csd", *args, **kwargs)
