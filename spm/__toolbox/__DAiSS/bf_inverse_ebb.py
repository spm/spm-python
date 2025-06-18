from mpython import Runtime


def bf_inverse_ebb(*args, **kwargs):
    """
      Computes Empirical Bayes Beamformer filters
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_ebb.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_inverse_ebb", *args, **kwargs)
