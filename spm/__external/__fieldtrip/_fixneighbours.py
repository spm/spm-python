from spm.__wrapper__ import Runtime


def _fixneighbours(*args, **kwargs):
  """  This function converts the old format of the neighbourstructure into the  
    new format - although it just works as a wrapper  
     
    See also FT_NEIGHBOURSELECTION  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixneighbours.m)
  """

  return Runtime.call("fixneighbours", *args, **kwargs)
