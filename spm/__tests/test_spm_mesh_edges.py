from spm.__wrapper__ import Runtime


def test_spm_mesh_edges(*args, **kwargs):
  """  Unit Tests for spm_mesh_edges  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_edges.m)
  """

  return Runtime.call("test_spm_mesh_edges", *args, **kwargs)
