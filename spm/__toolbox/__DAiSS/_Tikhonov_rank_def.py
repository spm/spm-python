from mpython import Runtime


def _Tikhonov_rank_def(*args, **kwargs):
    """
      Apply Tikhonov regularisation to rank-deficient matrix


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/Tikhonov_rank_def.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("Tikhonov_rank_def", *args, **kwargs)
