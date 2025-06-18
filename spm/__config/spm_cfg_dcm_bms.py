from mpython import Runtime


def spm_cfg_dcm_bms(*args, **kwargs):
    """
      Configuration file for Bayesian Model Selection (DCM)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_bms.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_dcm_bms", *args, **kwargs)
