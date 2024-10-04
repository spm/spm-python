from spm.__wrap__ import _Runtime


def _getorthoviewpos(*args, **kwargs):
  """  GETORTHOVIEWPOS obtains the orthographic projections of 3D positions  
    based on a given coordinate system and viewpoint  
     
    Use as  
      getorthoviewpos(pos, coordsys, viewpoint)  
     
    For example  
      getorthoviewpoint(pos, 'mni', 'superior')  
     
    See alo SETVIEWPOINT, COORDSYS2LABEL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/getorthoviewpos.m)
  """

  return _Runtime.call("getorthoviewpos", *args, **kwargs)
