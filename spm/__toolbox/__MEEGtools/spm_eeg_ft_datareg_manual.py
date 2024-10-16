from spm.__wrapper__ import Runtime


def spm_eeg_ft_datareg_manual(*args, **kwargs):
  """  Data registration user-interface routine  
    commands the EEG/MEG data co-registration within original sMRI space  
     
    FORMAT D = spm_eeg_inv_datareg_ui(D,[val], modality)  
    Input:  
    Output:  
    D         - same data struct including the new required files and variables  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_datareg_manual.m)
  """

  return Runtime.call("spm_eeg_ft_datareg_manual", *args, **kwargs)
