from spm.__wrap__ import _Runtime


def spm_eeg_lgainmat(*args, **kwargs):
  """  Load or compute if necessary a gain matrix  
    FORMAT [L,D] = spm_eeg_lgainmat(D,Is,channels)  
    D    - Data structure  
    Is   - indices of vertices  
     
    L    - Lead-field or gain matrix L(:,Is)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_lgainmat.m)
  """

  return _Runtime.call("spm_eeg_lgainmat", *args, **kwargs)
