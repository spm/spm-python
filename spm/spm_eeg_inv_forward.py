from spm.__wrap__ import _Runtime


def spm_eeg_inv_forward(*args, **kwargs):
  """  Compute M/EEG leadfield  
    FORMAT D = spm_eeg_inv_forward(D,val)  
     
    D                - input struct  
    (optional) fields of S:  
    D                - filename of EEG/MEG mat-file  
     
    Output:  
    D                - EEG/MEG struct with filenames of Gain matrices)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_forward.m)
  """

  return _Runtime.call("spm_eeg_inv_forward", *args, **kwargs)
