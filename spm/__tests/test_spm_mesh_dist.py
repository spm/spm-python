from spm.__wrap__ import _Runtime


def test_spm_mesh_dist(*args, **kwargs):
  """  Unit Tests for spm_mesh_dist  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_dist.m)
  """

  return _Runtime.call("test_spm_mesh_dist", *args, **kwargs)
