from mpython import Runtime


def bf_regularise_manual(*args, **kwargs):
    """
      Manual specification of the regularisation parameter
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_manual.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_regularise_manual", *args, **kwargs)
