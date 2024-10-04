from spm.__wrap__ import _Runtime


def spm_cfg_model_review(*args, **kwargs):
  """  SPM Configuration file for Model Review  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_model_review.m)
  """

  return _Runtime.call("spm_cfg_model_review", *args, **kwargs)
