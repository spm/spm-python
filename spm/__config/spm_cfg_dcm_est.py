from spm._runtime import Runtime


def spm_cfg_dcm_est(*args, **kwargs):
    """
      SPM Configuration file for DCM estimation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_est.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_dcm_est", *args, **kwargs)
