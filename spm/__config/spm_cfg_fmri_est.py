from spm._runtime import Runtime


def spm_cfg_fmri_est(*args, **kwargs):
    """
      SPM Configuration file for Model Estimation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_est.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_fmri_est", *args, **kwargs)
