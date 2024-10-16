from spm.__wrapper__ import Runtime


def _nearest_vec(*args, **kwargs):
  """  locate bilateral coordinate  
    Copyright (C) 2022 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nearest_vec.m)
  """

  return Runtime.call("nearest_vec", *args, **kwargs)
