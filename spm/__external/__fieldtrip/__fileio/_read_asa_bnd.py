from spm.__wrap__ import _Runtime


def _read_asa_bnd(*args, **kwargs):
  """  READ_ASA_BND reads an ASA boundary triangulation file  
    converting the units of the vertices to mm  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_asa_bnd.m)
  """

  return _Runtime.call("read_asa_bnd", *args, **kwargs)
