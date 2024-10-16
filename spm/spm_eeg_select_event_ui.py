from spm.__wrapper__ import Runtime


def spm_eeg_select_event_ui(*args, **kwargs):
  """  Allow the user to select an event using GUI  
    FORMAT selected = spm_eeg_select_event_ui(event)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_select_event_ui.m)
  """

  return Runtime.call("spm_eeg_select_event_ui", *args, **kwargs)
