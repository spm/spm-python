from spm.__wrapper__ import Runtime


def _read_serial_event(*args, **kwargs):
  """  READ_SERIAL_EVENT  
     
    changed A.Hadjipapas 2010  
     
    The only thing transmitted is the event.value (no info about sample) but it works  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_serial_event.m)
  """

  return Runtime.call("read_serial_event", *args, **kwargs)
