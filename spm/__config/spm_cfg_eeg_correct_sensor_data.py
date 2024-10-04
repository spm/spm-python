from spm.__wrap__ import _Runtime


def spm_cfg_eeg_correct_sensor_data(*args, **kwargs):
  """  Configuration file for coorecting sensor data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_correct_sensor_data.m)
  """

  return _Runtime.call("spm_cfg_eeg_correct_sensor_data", *args, **kwargs)
