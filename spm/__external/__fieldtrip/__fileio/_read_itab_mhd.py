from spm.__wrapper__ import Runtime


def _read_itab_mhd(*args, **kwargs):
  """read_itab_mhd is a function.  
      mhd = read_itab_mhd(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_itab_mhd.m)
  """

  return Runtime.call("read_itab_mhd", *args, **kwargs)
