from spm.__wrapper__ import Runtime


def _fixsegmentation(*args, **kwargs):
  """  FIXSEGMENTATION is a helper function that ensures the segmentation to be internally  
    consistent. It is used by FT_DATATYPE_SEGMENTATION and FT_DATATYPE_PARCELLATION.  
     
    % See also CONVERT_SEGMENTATIONSTYLE, DETERMINE_SEGMENTATIONSTYLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixsegmentation.m)
  """

  return Runtime.call("fixsegmentation", *args, **kwargs)
