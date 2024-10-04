from spm.__wrap__ import _Runtime


def _read_stl(*args, **kwargs):
  """  READ_STL reads a triangulation from an ascii or binary *.stl file, which  
    is a file format native to the stereolithography CAD software created by  
    3D Systems.  
     
    Use as  
      [pnt, tri, nrm] = read_stl(filename)  
     
    The format is described at http://en.wikipedia.org/wiki/STL_(file_format)  
     
    See also WRITE_STL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_stl.m)
  """

  return _Runtime.call("read_stl", *args, **kwargs)
