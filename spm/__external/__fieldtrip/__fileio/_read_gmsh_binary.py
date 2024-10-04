from spm.__wrap__ import _Runtime


def _read_gmsh_binary(*args, **kwargs):
  """  READ_GMSH_BINARY reads a gmsh .msh binary file. Current support is only  
    for version 2. There are some ASCII-readers floating around on the net,  
    but they do not seem to work with the primary use case in FieldTrip (and  
    the test data that I have available), which is SimNibs generated data.  
     
    See also MESH_LOAD_GMSH4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_gmsh_binary.m)
  """

  return _Runtime.call("read_gmsh_binary", *args, **kwargs)
