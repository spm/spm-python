from mpython import Runtime


def bf_features(*args, **kwargs):
    """
      Prepare data features for filter computation
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features", *args, **kwargs)
