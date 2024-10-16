from spm.__wrapper__ import Runtime


def _fixpos(*args, **kwargs):
  """  FIXPOS helper function to ensure that meshes are described properly  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixpos.m)
  """

  return Runtime.call("fixpos", *args, **kwargs)
