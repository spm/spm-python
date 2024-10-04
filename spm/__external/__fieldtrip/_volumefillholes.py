from spm.__wrap__ import _Runtime


def _volumefillholes(*args, **kwargs):
  """  VOLUMEFILLHOLES is a helper function for segmentations  
     
    See also VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD, VOLUMESELECTLARGEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumefillholes.m)
  """

  return _Runtime.call("volumefillholes", *args, **kwargs)
