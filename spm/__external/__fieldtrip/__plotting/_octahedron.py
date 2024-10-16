from spm.__wrapper__ import Runtime


def _octahedron(*args, **kwargs):
  """  OCTAHEDRON  
     
    Use as  
      [pos tri] = octahedron;  
     
    See also TETRAHEDRON ICOSAHEDRON  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/octahedron.m)
  """

  return Runtime.call("octahedron", *args, **kwargs)
