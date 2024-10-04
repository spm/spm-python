from spm.__wrap__ import _Runtime


def _read_ah5_data(*args, **kwargs):
  """read_ah5_data is a function.  
      [data] = read_ah5_data(filename, hdr, begsample, endsample, chanindx)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ah5_data.m)
  """

  return _Runtime.call("read_ah5_data", *args, **kwargs)
