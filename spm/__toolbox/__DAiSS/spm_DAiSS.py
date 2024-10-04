from spm.__wrap__ import _Runtime


def spm_DAiSS(*args, **kwargs):
  """ __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/spm_DAiSS.m)
  """

  return _Runtime.call("spm_DAiSS", *args, **kwargs, nargout=0)
