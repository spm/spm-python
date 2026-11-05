from spm._runtime import Runtime


def bf_view_glass(*args, **kwargs):
    r"""
      Diplays glass brain plot of DAISS output results  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_view_glass.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_view_glass", *args, **kwargs)
