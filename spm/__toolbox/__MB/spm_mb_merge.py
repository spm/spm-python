from spm._runtime import Runtime


def spm_mb_merge(*args, **kwargs):
    r"""
      Combine tissue maps together  
        FORMAT out = spm_mb_merge(cfg)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/spm_mb_merge.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mb_merge", *args, **kwargs)
