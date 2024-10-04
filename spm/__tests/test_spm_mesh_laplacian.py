from spm.__wrap__ import _Runtime


def test_spm_mesh_laplacian(*args, **kwargs):
  """  Unit Tests for spm_mesh_laplacian  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_mesh_laplacian.m)
  """

  return _Runtime.call("test_spm_mesh_laplacian", *args, **kwargs)
