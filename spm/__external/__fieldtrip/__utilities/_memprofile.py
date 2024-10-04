from spm.__wrap__ import _Runtime


def _memprofile(*args, **kwargs):
  """  MEMPROFILE this is a dummy placeholder  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/memprofile.m)
  """

  return _Runtime.call("memprofile", *args, **kwargs)
