from spm._runtime import Runtime


def bf_group_batch(*args, **kwargs):
    r"""
      Run a DAiSS batch on a group of subjects  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_group_batch.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_group_batch", *args, **kwargs)
