from spm.__wrap__ import _Runtime


def spm_eeg_erp_correction(*args, **kwargs):
  """  Applies corrections to ERPs or single trials as in DCM-ERP  
    This can be used to make a sensor level analysis or source reconstruction  
    consistent with DCM.  
    FORMAT D = spm_eeg_erp_correction(S)  
     
    S        - optional input struct  
    (optional) fields of S:  
    S.D        - MEEG object or filename of M/EEG mat-file with epoched data  
    S.detrend  - detrending order (0 for no detrending)  
    S.hanning  - apply Hanning window (true or false)  
    S.chtype   - channel type (default 'MEEG')  
     
    Output:  
    D        - MEEG object (also written on disk)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_erp_correction.m)
  """

  return _Runtime.call("spm_eeg_erp_correction", *args, **kwargs)
