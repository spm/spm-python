from spm.__wrap__ import _Runtime


def _read_tdt_tbk(*args, **kwargs):
  """  tbk file has block events information and time marks  
    for efficiently locate event if query by time  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tbk.m)
  """

  return _Runtime.call("read_tdt_tbk", *args, **kwargs)
