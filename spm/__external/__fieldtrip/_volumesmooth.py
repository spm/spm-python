from spm.__wrapper__ import Runtime


def _volumesmooth(*args, **kwargs):
  """  VOLUMESMOOTH is a helper function for segmentations  
     
    See also VOLUMETHRESHOLD, VOLUMEFILLHOLES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumesmooth.m)
  """

  return Runtime.call("volumesmooth", *args, **kwargs)
