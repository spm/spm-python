from spm.__wrap__ import _Runtime


def spm_eeg_inv_extract_ui(*args, **kwargs):
  """  GUI for contrast of evoked responses and power for an MEG-EEG model  
    FORMAT [D] = spm_eeg_inv_extract_ui(D, val, XYZ)  
    Sets:  
     
        D.contrast.woi   - time (ms) window of interest  
        D.contrast.fboi  - freq (Hz) window of interest  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_extract_ui.m)
  """

  return _Runtime.call("spm_eeg_inv_extract_ui", *args, **kwargs)
