from spm.__wrap__ import _Runtime


def _read_vtk(*args, **kwargs):
  """  READ_VTK reads a triangulation from a VTK (Visualisation ToolKit) format file  
    Supported are triangles and other polygons.  
     
    Use as  
      [pnt, tri] = read_vtk(filename)  
     
    See also WRITE_VTK  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_vtk.m)
  """

  return _Runtime.call("read_vtk", *args, **kwargs)
