from spm.__wrapper__ import Runtime


def _savevar(*args, **kwargs):
  """  SAVEVAR is a helper function for cfg.outputfile  
     
    See also LOADVAR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/savevar.m)
  """

  return Runtime.call("savevar", *args, **kwargs, nargout=0)
