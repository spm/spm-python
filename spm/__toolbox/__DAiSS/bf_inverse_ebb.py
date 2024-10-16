from spm.__wrapper__ import Runtime


def bf_inverse_ebb(*args, **kwargs):
  """  Computes Empirical Bayes Beamformer filters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_ebb.m)
  """

  return Runtime.call("bf_inverse_ebb", *args, **kwargs)
