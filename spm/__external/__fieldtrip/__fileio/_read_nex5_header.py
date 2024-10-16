from spm.__wrapper__ import Runtime


def _read_nex5_header(*args, **kwargs):
  """  READ_NEX5_HEADER for Nex Technologies *.nex5 file  
     
    Use as  
      [hdr] = read_nex5_header(filename)  
     
    See also RAD_NEX5_DATA, READ_NEX5_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex5_header.m)
  """

  return Runtime.call("read_nex5_header", *args, **kwargs)
