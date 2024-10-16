from spm.__wrapper__ import Runtime


def _read_ah5_markers(*args, **kwargs):
  """read_ah5_markers is a function.  
      [event] = read_ah5_markers(hdr, filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ah5_markers.m)
  """

  return Runtime.call("read_ah5_markers", *args, **kwargs)
