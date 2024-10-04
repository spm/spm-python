from spm.__wrap__ import _Runtime


def _volumeselectlargest(*args, **kwargs):
  """  VOLUMESELECTLARGEST is a helper function for segmentations  
     
    See also VOLUMEFILLHOLES, VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeselectlargest.m)
  """

  return _Runtime.call("volumeselectlargest", *args, **kwargs)
