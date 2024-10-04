from spm.__wrap__ import _Runtime


def _savevar(*args, **kwargs):
  """  SAVEVAR is a helper function for cfg.outputfile  
     
    See also LOADVAR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/savevar.m)
  """

  return _Runtime.call("savevar", *args, **kwargs, nargout=0)
