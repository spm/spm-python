from spm.__wrapper__ import Runtime


def _cfg_mlbatch_appcfg_master(*args, **kwargs):
    """
    cfg_mlbatch_appcfg_master is a function.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_mlbatch_appcfg_master.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_mlbatch_appcfg_master", *args, **kwargs, nargout=0)
