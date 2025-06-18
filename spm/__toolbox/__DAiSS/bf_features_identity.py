from mpython import Runtime


def bf_features_identity(*args, **kwargs):
    """
      Identity matrix for cases when covariance is not necessary
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_identity.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features_identity", *args, **kwargs)
