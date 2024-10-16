from spm.__wrapper__ import Runtime


def _read_shm_header(*args, **kwargs):
  """  READ_SHM_HEADER reads the header in real-time from shared memory  
    this is a helper function for FT_READ_HEADER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_shm_header.m)
  """

  return Runtime.call("read_shm_header", *args, **kwargs)
