from spm.__wrap__ import _Runtime


def spm_eeg_inv_check(*args, **kwargs):
  """  Checks that the EEG/MEG .mat file structure is loaded properly and that  
    the particular inversion of interest has been specified  
     
    FORMAT [D,val] = spm_eeg_inv_check(D,[val])  
    Input:  
    S              - data structure or its filename  
    val            - model of interest (usually 1)  
    Output:  
    D              - data structure  
    val            - model of interest D.val  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_check.m)
  """

  return _Runtime.call("spm_eeg_inv_check", *args, **kwargs)
