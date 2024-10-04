from spm.__wrap__ import _Runtime


def _timestamp_plexon(*args, **kwargs):
  """  TIMESTAMP_PLEXON merge the low and high part of the timestamps  
    into a single uint64 value  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/timestamp_plexon.m)
  """

  return _Runtime.call("timestamp_plexon", *args, **kwargs)
