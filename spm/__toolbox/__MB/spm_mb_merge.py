from mpython import Runtime


def spm_mb_merge(*args, **kwargs):
    """
      Combine tissue maps together
        FORMAT out = spm_mb_merge(cfg)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_merge.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mb_merge", *args, **kwargs)
