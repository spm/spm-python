from spm._runtime import Runtime


def bf_view_surface(*args, **kwargs):
    r"""
      Diplay surface plot of DAISS output results  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_view_surface.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_view_surface", *args, **kwargs)
