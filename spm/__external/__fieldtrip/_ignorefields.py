from spm.__wrap__ import _Runtime


def _ignorefields(*args, **kwargs):
  """  IGNOREFIELDS returns a list of fields that can be present in the cfg structure that  
    should be ignored at various places in the code, e.g. for provenance, history,  
    size-checking, etc.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/ignorefields.m)
  """

  return _Runtime.call("ignorefields", *args, **kwargs)
