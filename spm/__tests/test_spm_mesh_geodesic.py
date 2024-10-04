from spm.__wrap__ import _Runtime


def test_spm_mesh_geodesic(*args, **kwargs):
  """  Unit Tests for spm_mesh_geodesic  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_geodesic.m)
  """

  return _Runtime.call("test_spm_mesh_geodesic", *args, **kwargs)
