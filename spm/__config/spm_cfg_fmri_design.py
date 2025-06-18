from mpython import Runtime


def spm_cfg_fmri_design(*args, **kwargs):
    """
      SPM Configuration file for fMRI model specification (design only)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_design.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_fmri_design", *args, **kwargs)
