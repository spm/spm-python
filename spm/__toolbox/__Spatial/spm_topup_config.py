from mpython import Runtime


def spm_topup_config(*args, **kwargs):
    """
      SPM Configuration file for Topup
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_topup_config.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_topup_config", *args, **kwargs)
