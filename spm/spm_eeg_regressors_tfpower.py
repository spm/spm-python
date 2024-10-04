from spm.__wrap__ import _Runtime


def spm_eeg_regressors_tfpower(*args, **kwargs):
  """  Generate regressors from power in TF dataset  
    FORMAT res = spm_eeg_regressors_tfpower(S)  
    S                     - input structure  
    fields of S:  
       S.D                - M/EEG object  
     
       Additional parameters can be defined specific for each plugin  
    Output:  
     res -  
      If no input is provided the plugin returns a cfg branch for itself  
     
      If input is provided the plugin returns  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_regressors_tfpower.m)
  """

  return _Runtime.call("spm_eeg_regressors_tfpower", *args, **kwargs)
