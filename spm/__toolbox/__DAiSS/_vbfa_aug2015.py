from spm.__wrapper__ import Runtime


def _vbfa_aug2015(*args, **kwargs):
  """  Output  
    Regularized noise covariance from pre-stimulus data  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/vbfa_aug2015.m)
  """

  return Runtime.call("vbfa", *args, **kwargs)
