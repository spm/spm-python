from mpython import Runtime


def bf_view_glass(*args, **kwargs):
    """
      Diplays glass brain plot of DAISS output results
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view_glass.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_view_glass", *args, **kwargs)
