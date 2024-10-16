from spm.__wrapper__ import Runtime


def spm_cfg_eeg_tf_rescale(*args, **kwargs):
  """  Configuration file for rescaling spectrograms  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_tf_rescale.m)
  """

  return Runtime.call("spm_cfg_eeg_tf_rescale", *args, **kwargs)
