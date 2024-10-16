from spm.__wrapper__ import Runtime


def _menu_viewpoint(*args, **kwargs):
  """  MENU_VIEWPOINT adds a context menu to a 3D figure.  
     
    See also MENU_FIELDTRIP  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/menu_viewpoint.m)
  """

  return Runtime.call("menu_viewpoint", *args, **kwargs, nargout=0)
