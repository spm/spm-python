from spm.__wrap__ import _Runtime


def _determine_segmentationstyle(*args, **kwargs):
  """  DETERMINE_SEGMENTATIONSTYLE is a helper function that determines the type of segmentation  
    contained in each of the fields. It is used by FT_DATATYPE_SEGMENTATION and  
    FT_DATATYPE_PARCELLATION.  
     
    See also FIXSEGMENTATION, CONVERT_SEGMENTATIONSTYLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/determine_segmentationstyle.m)
  """

  return _Runtime.call("determine_segmentationstyle", *args, **kwargs)
