from spm.__wrapper__ import Runtime


def spm_eeg_remove_bad_trials(*args, **kwargs):
  """  Physically removes trials marked as bad from the dataset  
    FORMAT D = spm_eeg_remove_bad_trials(S)  
     
    S        - optional input struct  
     fields of S:  
    D        - MEEG object or filename of M/EEG mat-file with epoched data  
    prefix   - prefix for the output file (default - 'r')  
     
    Output:  
    D        - MEEG object (also written on disk)  
     
    The function also changes the physical order of trials to conform to  
    condlist.  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_remove_bad_trials.m)
  """

  return Runtime.call("spm_eeg_remove_bad_trials", *args, **kwargs)
