from spm.__wrap__ import _Runtime


def _browse_movieplotER(*args, **kwargs):
  """  BROWSE_MOVIEPLOTER is a helper function for FT_DATABROWSER and makes a  
    movie of the data that was selected. See ft_movieplotER for further details  
    on the options that can be specified as cfg.selcfg in ft_databrowser.  
     
    See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_movieplotER.m)
  """

  return _Runtime.call("browse_movieplotER", *args, **kwargs, nargout=0)
