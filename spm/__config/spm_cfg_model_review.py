from spm.__wrapper__ import Runtime


def spm_cfg_model_review(*args, **kwargs):
  """  SPM Configuration file for Model Review  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_model_review.m)
  """

  return Runtime.call("spm_cfg_model_review", *args, **kwargs)
