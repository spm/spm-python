from spm.__wrapper__ import Runtime


def _browse_topoplotVAR(*args, **kwargs):
  """  BROWSE_TOPOPLOTVAR is a simple helper function for FT_DATABROWSER that  
    computes the variance of band-pass filtered data and makes a topographic  
    plot. It serves to make a quick-and-dirty power topography.  
     
    See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_topoplotVAR.m)
  """

  return Runtime.call("browse_topoplotVAR", *args, **kwargs, nargout=0)
