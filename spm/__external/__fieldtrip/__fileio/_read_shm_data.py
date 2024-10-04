from spm.__wrap__ import _Runtime


def _read_shm_data(*args, **kwargs):
  """  READ_SHM_DATA reads the data in real-time from shared memory  
    this is a helper function for READ_DATA  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_data.m)
  """

  return _Runtime.call("read_shm_data", *args, **kwargs)
