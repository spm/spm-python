from spm.__wrap__ import _Runtime


def _read_ahdf5_hdr(*args, **kwargs):
  """ read header  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ahdf5_hdr.m)
  """

  return _Runtime.call("read_ahdf5_hdr", *args, **kwargs)
