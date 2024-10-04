from spm.__wrap__ import _Runtime


def spm_cfg_eeg_pca_distort(*args, **kwargs):
  """  Configuration file for creating distorted versions of subject anatomy  
    Based on original antomical and predetermined 100 eigen component template space.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_pca_distort.m)
  """

  return _Runtime.call("spm_cfg_eeg_pca_distort", *args, **kwargs)
