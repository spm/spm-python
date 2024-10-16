from spm.__wrapper__ import Runtime


def _read_tdt_sev(*args, **kwargs):
  """  READ_TDT_SEV  
     
    Use as  
      sev = read_tdt_sev(filename, dtype, begsample, endsample)  
     
    Note: sev files contain raw broadband data that is streamed to the RS4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tdt_sev.m)
  """

  return Runtime.call("read_tdt_sev", *args, **kwargs)
