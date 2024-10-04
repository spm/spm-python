from spm.__wrap__ import _Runtime


def _loadvar(*args, **kwargs):
  """  LOADVAR is a helper function for cfg.inputfile  
     
    See also SAVEVAR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/loadvar.m)
  """

  return _Runtime.call("loadvar", *args, **kwargs)
