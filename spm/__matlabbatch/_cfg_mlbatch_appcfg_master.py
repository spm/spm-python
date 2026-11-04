from spm._runtime import Runtime


def _cfg_mlbatch_appcfg_master(*args, **kwargs):
    r"""
    cfg_mlbatch_appcfg_master is a function.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_mlbatch_appcfg_master.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_mlbatch_appcfg_master", *args, **kwargs, nargout=0)
