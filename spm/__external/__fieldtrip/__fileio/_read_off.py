from spm.__wrap__ import _Runtime


def _read_off(*args, **kwargs):
  """  READ_OFF reads vertices and triangles from a OFF format triangulation file  
     
    [pnt, tri] = read_off(filename)  
     
    See also READ_TRI, READ_BND  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_off.m)
  """

  return _Runtime.call("read_off", *args, **kwargs)
