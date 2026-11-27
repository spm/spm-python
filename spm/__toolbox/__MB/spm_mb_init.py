from spm._runtime import Runtime


def spm_mb_init(*args, **kwargs):
    r"""
      Initialisation of Multi-Brain data structures  
        FORMAT [dat,sett] = spm_mb_init(cfg)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/spm_mb_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mb_init", *args, **kwargs)
