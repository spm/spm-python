from spm.__wrap__ import _Runtime


def spm_eeg_regressors(*args, **kwargs):
  """  Prepare regressors for GLM analysis of M/EEG data  
    FORMAT regfile = spm_eeg_regressors(S)  
     
    S                     - input structure  
     
    fields of S:  
      S.D                 - MEEG object or filename of M/EEG mat-file   
                            for which the regressors should be prepared  
     
    Output:  
    regfile              - path to mat file in which the regressors are saved  
   __________________________________________________________________________  
     
    This is a modular function for which plugins can be developed  
    implementing specific regressor creation cases  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_regressors.m)
  """

  return _Runtime.call("spm_eeg_regressors", *args, **kwargs)
