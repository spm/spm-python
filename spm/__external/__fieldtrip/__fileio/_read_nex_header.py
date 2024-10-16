from spm.__wrapper__ import Runtime


def _read_nex_header(*args, **kwargs):
  """  READ_NEX_HEADER for Plexon *.nex file  
     
    Use as  
      [hdr] = read_nex_header(filename)  
     
    See also RAD_NEX_DATA, READ_NEX_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex_header.m)
  """

  return Runtime.call("read_nex_header", *args, **kwargs)
