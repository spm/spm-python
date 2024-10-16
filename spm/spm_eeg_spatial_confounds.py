from spm.__wrapper__ import Runtime


def spm_eeg_spatial_confounds(*args, **kwargs):
  """  This function defines spatial confounds and adds them to MEEG dataset.  
    FORMAT D = spm_eeg_spatial_confounds(S)  
     
    S        - optional input struct  
     fields of S:  
      D        - MEEG object or filename of M/EEG mat-file with epoched data  
      mode     - method for definition of the confounds (EYES, BESA, SVD,  
                 SPMEEG, CLEAR)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_spatial_confounds.m)
  """

  return Runtime.call("spm_eeg_spatial_confounds", *args, **kwargs)
