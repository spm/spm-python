from spm.__wrapper__ import Runtime


def spm_eeg_interpolate_artefact(*args, **kwargs):
  """  'Baseline Correction' for M/EEG data  
    FORMAT D = spm_eeg_interpolate_artefact(S)  
     
    S        - optional input struct  
    (optional) fields of S:  
      S.D    - MEEG object or filename of M/EEG mat-file with epoched data  
      S.time - 2-element vector with start and end of baseline period [ms]  
     
    D        - MEEG object (also saved on disk if requested)  
   __________________________________________________________________________  
     
    Subtract average baseline from all M/EEG and EOG channels  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_interpolate_artefact.m)
  """

  return Runtime.call("spm_eeg_interpolate_artefact", *args, **kwargs)
