from spm.__wrap__ import _Runtime


def spm_eeg_copy(*args, **kwargs):
  """  Copy EEG/MEG data to new files  
    FORMAT D = spm_eeg_copy(S)  
    S           - input struct (optional)  
     fields of S:  
      S.D       - MEEG object or filename of MEEG mat-file  
      S.outfile - filename for the new dataset  
      S.updatehistory - update history information [default: true]  
     
    D           - MEEG object of the new dataset  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_copy.m)
  """

  return _Runtime.call("spm_eeg_copy", *args, **kwargs)
