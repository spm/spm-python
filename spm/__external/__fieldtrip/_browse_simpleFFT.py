from spm.__wrapper__ import Runtime


def _browse_simpleFFT(*args, **kwargs):
  """  BROWSE_SIMPLEFFT is a helper function for FT_DATABROWSER that shows a  
    simple FFT of the data.  
     
    Included are a button to switch between log and non-log space, and a  
    selection button to deselect channels, for the purpose of zooming in on  
    bad channels.  
     
    See also BROWSE_MOVIEPLOTER, BROWSE_TOPOPLOTER, BROWSE_MULTIPLOTER, BROWSE_TOPOPLOTVAR, BROWSE_SIMPLEFFT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_simpleFFT.m)
  """

  return Runtime.call("browse_simpleFFT", *args, **kwargs, nargout=0)
