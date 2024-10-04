from spm.__wrap__ import _Runtime


def splint_gh(*args, **kwargs):
  """  SPLINT_GH implements equations (3) and (5b) of Perrin 1989  
    for simultaneous computation of multiple values  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/splint_gh.m)
  """

  return _Runtime.call("splint_gh", *args, **kwargs)
