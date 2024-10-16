from spm.__wrapper__ import Runtime


def spm_eeg_prep_ui(*args, **kwargs):
  """  User interface for spm_eeg_prep function performing several tasks  
    for preparation of converted MEEG data for further analysis  
    FORMAT spm_eeg_prep_ui(callback)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_prep_ui.m)
  """

  return Runtime.call("spm_eeg_prep_ui", *args, **kwargs, nargout=0)
