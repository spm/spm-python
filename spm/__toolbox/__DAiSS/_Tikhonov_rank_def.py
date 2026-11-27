from spm._runtime import Runtime


def _Tikhonov_rank_def(*args, **kwargs):
    r"""
      Apply Tikhonov regularisation to rank-deficient matrix  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/Tikhonov_rank_def.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("Tikhonov_rank_def", *args, **kwargs)
