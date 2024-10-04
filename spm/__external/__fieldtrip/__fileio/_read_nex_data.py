from spm.__wrap__ import _Runtime


def _read_nex_data(*args, **kwargs):
  """  READ_NEX_DATA for Plexon *.nex file  
     
    Use as  
      [dat] = read_nex_data(filename, hdr, begsample, endsample, chanindx)  
     
    See also READ_NEX_HEADER, READ_NEX_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex_data.m)
  """

  return _Runtime.call("read_nex_data", *args, **kwargs)
