from spm.__wrap__ import _Runtime


def _select3dtool(*args, **kwargs):
  """ SELECT3DTOOL A simple tool for interactively obtaining 3-D coordinates   
     
    SELECT3DTOOL(FIG) Specify figure handle  
     
    Example:  
      surf(peaks);  
      select3dtool;  
      % click on surface  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/select3dtool.m)
  """

  return _Runtime.call("select3dtool", *args, **kwargs, nargout=0)
