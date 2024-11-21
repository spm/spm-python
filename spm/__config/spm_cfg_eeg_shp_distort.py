from spm.__wrapper__ import Runtime


def spm_cfg_eeg_shp_distort(*args, **kwargs):
    """
      Configuration file for creating distorted versions of subject anatomy  
        Based on original antomical and predetermined 100 eigen component template space.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_shp_distort.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_shp_distort", *args, **kwargs)
