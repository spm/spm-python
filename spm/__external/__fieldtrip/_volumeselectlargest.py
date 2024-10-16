from spm.__wrapper__ import Runtime


def _volumeselectlargest(*args, **kwargs):
  """  VOLUMESELECTLARGEST is a helper function for segmentations  
     
    See also VOLUMEFILLHOLES, VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeselectlargest.m)
  """

  return Runtime.call("volumeselectlargest", *args, **kwargs)
