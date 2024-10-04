from spm.__wrap__ import _Runtime


def _reproducescript(*args, **kwargs):
  """  This is a helper function to create a script that reproduces the analysis. It  
    appends the configuration and the function call to a MATLAB script.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/reproducescript.m)
  """

  return _Runtime.call("reproducescript", *args, **kwargs, nargout=0)
