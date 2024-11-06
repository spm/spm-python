from spm.__wrapper__ import Runtime


def _Tikhonov_rank_def(*args, **kwargs):
    """
      Apply Tikhonov regularisation to rank-deficient matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/Tikhonov_rank_def.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("Tikhonov_rank_def", *args, **kwargs)
