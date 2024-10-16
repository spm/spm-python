from spm.__wrapper__ import Runtime


def _volumepad(*args, **kwargs):
  """  VOLUMEPAR is a helper function for segmentations. It adds a layer on all sides to  
    ensure that the tissue can be meshed all the way up to the edges this also ensures  
    that the mesh at the bottom of the neck will be closed.  
     
    See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMETHRESHOLD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumepad.m)
  """

  return Runtime.call("volumepad", *args, **kwargs)
