from spm.__wrapper__ import Runtime


def spm_cfg_eeg_pca_distort(*args, **kwargs):
  """  Configuration file for creating distorted versions of subject anatomy  
    Based on original antomical and predetermined 100 eigen component template space.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_pca_distort.m)
  """

  return Runtime.call("spm_cfg_eeg_pca_distort", *args, **kwargs)
