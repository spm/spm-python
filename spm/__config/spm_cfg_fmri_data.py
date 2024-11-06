from spm.__wrapper__ import Runtime


def spm_cfg_fmri_data(*args, **kwargs):
    """
      SPM Configuration file for fMRI data specification  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_fmri_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_fmri_data", *args, **kwargs)
