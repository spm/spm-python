from spm.__wrap__ import _Runtime


def spm_eeg_reduce_whiten(*args, **kwargs):
  """  Plugin for data whitening  
    FORMAT res = spm_eeg_reduce_pca(S)  
     
    S                     - input structure  
    fields of S:  
       S.ncomp            - number of PCA components  
     
    Output:  
     res -  
      If no input is provided the plugin returns a cfg branch for itself  
     
      If input is provided:  
         montage struct implementing data whitening  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_reduce_whiten.m)
  """

  return _Runtime.call("spm_eeg_reduce_whiten", *args, **kwargs)
