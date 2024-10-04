from spm.__wrap__ import _Runtime


def spm_eeg_inv_imag_api(*args, **kwargs):
  """  API for EEG/MEG source reconstruction interface  
    FORMAT:  
       FIG = SPM_EEG_INV_IMAG_API launch spm_eeg_inv_imag_api GUI.  
       SPM_EEG_INV_IMAG_API('callback_name', ...) invoke the named callback.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_imag_api.m)
  """

  return _Runtime.call("spm_eeg_inv_imag_api", *args, **kwargs)
