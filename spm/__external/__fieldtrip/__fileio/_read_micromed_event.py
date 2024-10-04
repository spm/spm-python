from spm.__wrap__ import _Runtime


def _read_micromed_event(*args, **kwargs):
  """  reads the events of the Micromed TRC format files  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_micromed_event.m)
  """

  return _Runtime.call("read_micromed_event", *args, **kwargs)
