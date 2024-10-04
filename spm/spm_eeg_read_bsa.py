from spm.__wrap__ import _Runtime


def spm_eeg_read_bsa(*args, **kwargs):
  """  This function reads a definition of spatial confounds from a BESA  
    *.bsa file and returns an sconfounds struct with the following fields  
    .label - labels of channels  
    .coeff - matrix of coefficients (channels x components)  
    .bad - logical vector - channels marked as bad.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_read_bsa.m)
  """

  return _Runtime.call("spm_eeg_read_bsa", *args, **kwargs)
