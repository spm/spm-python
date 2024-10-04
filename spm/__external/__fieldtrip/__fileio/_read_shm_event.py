from spm.__wrap__ import _Runtime


def _read_shm_event(*args, **kwargs):
  """  READ_SHM_EVENT reads the events in real-time from shared memory  
    this is a helper function for READ_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_event.m)
  """

  return _Runtime.call("read_shm_event", *args, **kwargs)
