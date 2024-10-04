from spm.__wrap__ import _Runtime


def _volumesmooth(*args, **kwargs):
  """  VOLUMESMOOTH is a helper function for segmentations  
     
    See also VOLUMETHRESHOLD, VOLUMEFILLHOLES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumesmooth.m)
  """

  return _Runtime.call("volumesmooth", *args, **kwargs)
