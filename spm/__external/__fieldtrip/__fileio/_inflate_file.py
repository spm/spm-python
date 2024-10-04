from spm.__wrap__ import _Runtime


def _inflate_file(*args, **kwargs):
  """  INFLATE_FILE helper function to uncompress a compressed file of arbitrary  
    compression type. Returns the full path to the extracted file or  
    directory, which will be located in a temporary location.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/inflate_file.m)
  """

  return _Runtime.call("inflate_file", *args, **kwargs)
