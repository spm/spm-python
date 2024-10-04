from spm.__wrap__ import _Runtime


def _write_serial_event(*args, **kwargs):
  """  WRITE_SERIAL_EVENT  
     
    changed A.Hadjipapas 2010  
     
    write to phyiscal serial port  
    serial port on windows or linux platform  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_serial_event.m)
  """

  return _Runtime.call("write_serial_event", *args, **kwargs, nargout=0)
