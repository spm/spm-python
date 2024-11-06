from spm.__wrapper__ import Runtime


def spm_cfg_eeg_correct_sensor_data(*args, **kwargs):
    """
      Configuration file for coorecting sensor data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_correct_sensor_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_correct_sensor_data", *args, **kwargs)
