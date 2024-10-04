from spm.__wrap__ import _Runtime


def spm_eeg_ft_megplanar(*args, **kwargs):
  """  Function for transforming MEG data to planar gradient  
     
    FORMAT  D = spm_eeg_ft_megplanar(S)  
     
    S           - input structure (optional)  
    (optional) fields of S:  
      S.D       - filename, or M/EEG object  
      S.prefix  - prefix (default L)  
     
    Output  
      D - dataset converted to planar gradient  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_megplanar.m)
  """

  return _Runtime.call("spm_eeg_ft_megplanar", *args, **kwargs)
