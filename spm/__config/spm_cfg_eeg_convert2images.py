from spm.__wrapper__ import Runtime


def spm_cfg_eeg_convert2images(*args, **kwargs):
    """
      Configuration file for writing voxel-based images from SPM M/EEG format,  
        as a time-series of 2Dimages  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_convert2images.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_convert2images", *args, **kwargs)
