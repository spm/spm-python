from spm.__wrap__ import _Runtime


def bf_features_cov_bysamples(*args, **kwargs):
  """  Simple covariance computation to handle variable width WOIs,   
    Requires S.samples as a [1 x samples x ntrials] matrix of logical indices  
    indicating which data points should be used in the cov estimation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_cov_bysamples.m)
  """

  return _Runtime.call("bf_features_cov_bysamples", *args, **kwargs)
