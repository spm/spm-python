from spm.__wrap__ import _Runtime


def _jaga16_packet(*args, **kwargs):
  """  JAGA16_PACKET converts the JAGA16 byte stream into packets  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/jaga16_packet.m)
  """

  return _Runtime.call("jaga16_packet", *args, **kwargs)
