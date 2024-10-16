from spm.__wrapper__ import Runtime


def _read_tdt_tdx(*args, **kwargs):
  """  tdx file contains just information about epoc,  
    is generated after recording if necessary for fast retrieve epoc information  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_tdx.m)
  """

  return Runtime.call("read_tdt_tdx", *args, **kwargs)
