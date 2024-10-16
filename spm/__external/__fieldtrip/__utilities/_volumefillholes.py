from spm.__wrapper__ import Runtime


def _volumefillholes(*args, **kwargs):
  """  VOLUMEFILLHOLES is a helper function for segmentations  
     
    See also VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD, VOLUMESELECTLARGEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumefillholes.m)
  """

  return Runtime.call("volumefillholes", *args, **kwargs)
