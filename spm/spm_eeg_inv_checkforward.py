from spm.__wrap__ import _Runtime


def spm_eeg_inv_checkforward(*args, **kwargs):
  """  Check M/EEG forward model  
    FORMAT spm_eeg_inv_checkforward(D, val, ind)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_checkforward.m)
  """

  return _Runtime.call("spm_eeg_inv_checkforward", *args, **kwargs, nargout=0)
