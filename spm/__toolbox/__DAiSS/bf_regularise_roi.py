from mpython import Runtime


def bf_regularise_roi(*args, **kwargs):
    """
      ROI regularisation


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_roi.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_regularise_roi", *args, **kwargs)
