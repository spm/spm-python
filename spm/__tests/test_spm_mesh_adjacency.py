from spm.__wrapper__ import Runtime


def test_spm_mesh_adjacency(*args, **kwargs):
  """  Unit Tests for spm_mesh_adjacency  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_adjacency.m)
  """

  return Runtime.call("test_spm_mesh_adjacency", *args, **kwargs)
