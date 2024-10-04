from spm.__wrap__ import _Runtime


def test_spm_mesh_neighbours(*args, **kwargs):
  """  Unit Tests for spm_mesh_neighbours  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_neighbours.m)
  """

  return _Runtime.call("test_spm_mesh_neighbours", *args, **kwargs)
