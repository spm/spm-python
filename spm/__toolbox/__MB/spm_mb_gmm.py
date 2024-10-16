from spm.__wrapper__ import Runtime


def spm_mb_gmm(*args, **kwargs):
  """   
    FORMAT varargout = spm_mb_gmm(varargin)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_gmm.m)
  """

  return Runtime.call("spm_mb_gmm", *args, **kwargs)
