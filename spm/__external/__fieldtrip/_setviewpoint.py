from spm.__wrap__ import _Runtime


def _setviewpoint(*args, **kwargs):
  """  SETVIEWPOINT changes the viewpoint for a 3D image that contains data in a known coordinate system  
     
    Use as  
      setviewpoint(ax, coordsys, viewpoint)  
     
    For example  
      setviewpoint(gca, 'mni', 'left')  
     
    See alo GETORTHOVIEWPOS, COORDSYS2LABEL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/setviewpoint.m)
  """

  return _Runtime.call("setviewpoint", *args, **kwargs, nargout=0)
