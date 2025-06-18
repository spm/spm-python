from mpython import Runtime


def bf_regularise_mantrunc(*args, **kwargs):
    """
      User-specified dimensional reduction
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_mantrunc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_regularise_mantrunc", *args, **kwargs)
