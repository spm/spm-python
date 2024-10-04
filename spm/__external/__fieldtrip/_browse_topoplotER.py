from spm.__wrap__ import _Runtime


def _browse_topoplotER(*args, **kwargs):
  """  BROWSE_TOPOPLOTER is a simple helper function for FT_DATABROWSER and shows  
    the average topography of the selected data.  
     
    See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_topoplotER.m)
  """

  return _Runtime.call("browse_topoplotER", *args, **kwargs, nargout=0)
