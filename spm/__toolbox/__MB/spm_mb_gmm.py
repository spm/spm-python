from spm.__wrap__ import _Runtime


def spm_mb_gmm(*args, **kwargs):
  """   
    FORMAT varargout = spm_mb_gmm(varargin)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_gmm.m)
  """

  return _Runtime.call("spm_mb_gmm", *args, **kwargs)
