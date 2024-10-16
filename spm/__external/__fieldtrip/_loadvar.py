from spm.__wrapper__ import Runtime


def _loadvar(*args, **kwargs):
  """  LOADVAR is a helper function for cfg.inputfile  
     
    See also SAVEVAR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/loadvar.m)
  """

  return Runtime.call("loadvar", *args, **kwargs)
