from spm.__wrap__ import _Runtime


def _fixneighbours(*args, **kwargs):
  """  This function converts the old format of the neighbourstructure into the  
    new format - although it just works as a wrapper  
     
    See also FT_NEIGHBOURSELECTION  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixneighbours.m)
  """

  return _Runtime.call("fixneighbours", *args, **kwargs)
