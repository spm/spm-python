from mpython import Runtime


def cfg_mlbatch_appcfg(*args, **kwargs):
    """
      Add SPM to the application list of MATLABBATCH
        This file must be on MATLAB search path for cfg_util to detect it.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/cfg_mlbatch_appcfg.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_mlbatch_appcfg", *args, **kwargs)
