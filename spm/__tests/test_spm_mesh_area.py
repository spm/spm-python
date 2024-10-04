from spm.__wrap__ import _Runtime


def test_spm_mesh_area(*args, **kwargs):
  """  Unit Tests for spm_mesh_area  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_area.m)
  """

  return _Runtime.call("test_spm_mesh_area", *args, **kwargs)
