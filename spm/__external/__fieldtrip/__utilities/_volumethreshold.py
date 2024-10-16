from spm.__wrapper__ import Runtime


def _volumethreshold(*args, **kwargs):
  """  VOLUMETHRESHOLD is a helper function for segmentations. It applies a  
    relative threshold and subsequently looks for the largest connected part,  
    thereby removing small blobs such as vitamine E capsules.  
     
    See also VOLUMEFILLHOLES, VOLUMESMOOTH, VOLUMEPAD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumethreshold.m)
  """

  return Runtime.call("volumethreshold", *args, **kwargs)
