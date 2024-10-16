from spm.__wrapper__ import Runtime


def spm_cfg_preproc8(*args, **kwargs):
  """  Configuration file for 'Combined Segmentation and Spatial Normalisation'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_preproc8.m)
  """

  return Runtime.call("spm_cfg_preproc8", *args, **kwargs)
