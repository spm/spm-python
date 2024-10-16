from spm.__wrapper__ import Runtime


def bf_regularise_clifftrunc(*args, **kwargs):
  """  Regularisation based on the sudden drop-off in the covariance Eigenspectrum  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_clifftrunc.m)
  """

  return Runtime.call("bf_regularise_clifftrunc", *args, **kwargs)
