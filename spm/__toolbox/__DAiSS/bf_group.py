from spm._runtime import Runtime


def bf_group(*args, **kwargs):
    r"""
      A module for applying a processing step to a group of subjects  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_group.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_group", *args, **kwargs)
