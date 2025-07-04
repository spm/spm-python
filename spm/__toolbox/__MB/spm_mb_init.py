from spm._runtime import Runtime


def spm_mb_init(*args, **kwargs):
    """
      Initialisation of Multi-Brain data structures  
        FORMAT [dat,sett] = spm_mb_init(cfg)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_init.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mb_init", *args, **kwargs)
