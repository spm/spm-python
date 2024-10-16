from spm.__wrapper__ import Runtime


def _write_off(*args, **kwargs):
  """  WRITE_OFF writes a set of geometrical planar forms (called piecewise linear complex, PLC)  
    to an ascii *.off file, which is a file format created by Princeton Shape Benchmark  
     
    Use as  
      write_stl(filename, pnt, tri)  
     
    See also READ_OFF  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_off.m)
  """

  return Runtime.call("write_off", *args, **kwargs, nargout=0)
