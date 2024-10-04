from spm.__wrap__ import _Runtime


def _ftcolors(*args, **kwargs):
  """  FTCOLORS returns an Nx3 rgb matrix with the  
    colors of the fieldtrip logo at its extremes.  
    Can be used as a colormap by FT_COLORMAP  
     
    Use as:  
      rgb = ftcolors(N), or  
      rgb = ftcolors  
     
    Without input arguments, N will be set to 64  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/ftcolors.m)
  """

  return _Runtime.call("ftcolors", *args, **kwargs)
