from spm._runtime import Runtime


def tbx_cfg_mb(*args, **kwargs):
    r"""
      MATLABBATCH Configuration file for toolbox 'Multi-Brain'  
       _____________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/tbx_cfg_mb.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_mb", *args, **kwargs)
