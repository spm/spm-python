from spm.__wrap__ import _Runtime


def _buffer_wait_dat(*args, **kwargs):
  """  BUFFER_WAIT_DAT implementation that is also backwards compatibility with ft buffer version 1  
     
    Use as  
      available = buffer_wait_dat(selection, host, port)  
    where  
      selection(1) = nsamples, 0 indicates not to wait  
      selection(2) = nevents,  0 indicates not to wait  
      selection(3) = timeout in seconds  
     
    It returns a structure with the available nsamples and nevents.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/buffer_wait_dat.m)
  """

  return _Runtime.call("buffer_wait_dat", *args, **kwargs)
