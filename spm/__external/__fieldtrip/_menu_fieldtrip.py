from spm.__wrapper__ import Runtime


def _menu_fieldtrip(*args, **kwargs):
  """  MENU_FIELDTRIP adds a FieldTrip-specific menu to a figure.  
     
    See also MENU_VIEWPOINT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/menu_fieldtrip.m)
  """

  return Runtime.call("menu_fieldtrip", *args, **kwargs, nargout=0)
