from spm.__wrap__ import _Runtime


def spm_eeg_fuse(*args, **kwargs):
  """  Fuse MEG and EEG datasets to create a multimodal dataset  
    FORMAT D = spm_eeg_fuse(S)  
     
    S           - input structure (optional)  
     fields of S:  
      S.D       - character array containing filenames of M/EEG mat-files  
      S.prefix     - prefix for the output file (default - 'u')  
     
    D        - MEEG object (also written to disk, with a 'u' prefix)  
   __________________________________________________________________________  
     
    Vladimir Litvak  
    Copyright (C) 2008-2022 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_fuse.m)
  """

  return _Runtime.call("spm_eeg_fuse", *args, **kwargs)
