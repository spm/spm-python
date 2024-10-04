from spm.__wrap__ import _Runtime


def spm_eeg_tms_correct(*args, **kwargs):
  """  Function for removing TMS artefacts  
    FORMAT D = spm_eeg_tms_correct(S)  
    S                    - input structure (optional)  
    (optional) fields of S:  
      S.D                - MEEG object or filename of M/EEG mat-file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_tms_correct.m)
  """

  return _Runtime.call("spm_eeg_tms_correct", *args, **kwargs)
