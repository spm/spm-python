from spm.__wrap__ import _Runtime


def _fixpos(*args, **kwargs):
  """  FIXPOS helper function to ensure that meshes are described properly  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fixpos.m)
  """

  return _Runtime.call("fixpos", *args, **kwargs)
