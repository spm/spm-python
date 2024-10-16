from spm.__wrapper__ import Runtime


def _write_stl(*args, **kwargs):
  """  WRITE_STL writes a triangulation to an ascii *.stl file, which is a file  
    format native to the stereolithography CAD software created by 3D Systems.  
     
    Use as  
      write_stl(filename, pnt, tri, nrm)  
    where nrm refers to the triangle normals.  
     
    See also READ_STL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_stl.m)
  """

  return Runtime.call("write_stl", *args, **kwargs, nargout=0)
