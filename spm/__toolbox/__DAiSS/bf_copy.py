from spm._runtime import Runtime


def bf_copy(*args, **kwargs):
    r"""
      Set up a new analysis by copying an existing one  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_copy.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_copy", *args, **kwargs)
