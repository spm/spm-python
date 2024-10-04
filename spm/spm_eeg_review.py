from spm.__wrap__ import _Runtime


def spm_eeg_review(*args, **kwargs):
  """  General review (display) of SPM meeg object  
    FORMAT spm_eeg_review(D,flags,inv)  
     
    INPUT:  
    D      - meeg object  
    flag   - switch to any of the displays (optional)  
    inv    - which source reconstruction to display (when called from  
    spm_eeg_inv_imag_api.m)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_review.m)
  """

  return _Runtime.call("spm_eeg_review", *args, **kwargs, nargout=0)
