from spm.__wrapper__ import Runtime


def spm_cfg_eeg_correct_sensor_data(*args, **kwargs):
  """  Configuration file for coorecting sensor data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_correct_sensor_data.m)
  """

  return Runtime.call("spm_cfg_eeg_correct_sensor_data", *args, **kwargs)
