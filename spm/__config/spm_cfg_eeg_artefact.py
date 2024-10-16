from spm.__wrapper__ import Runtime


def spm_cfg_eeg_artefact(*args, **kwargs):
  """  Configuration file for M/EEG artefact detection  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_artefact.m)
  """

  return Runtime.call("spm_cfg_eeg_artefact", *args, **kwargs)
