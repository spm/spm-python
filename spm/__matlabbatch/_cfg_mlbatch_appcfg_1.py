from spm._runtime import Runtime


def _cfg_mlbatch_appcfg_1(*args, **kwargs):
    r"""
      Add SPM to the application list of MATLABBATCH  
        This file must be on MATLAB search path for cfg_util to detect it.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_mlbatch_appcfg_1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_mlbatch_appcfg", *args, **kwargs)
