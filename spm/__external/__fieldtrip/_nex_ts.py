from spm.__wrapper__ import Runtime


def _nex_ts(*args, **kwargs):
  """  nex_ts(filename, varname): Read timestamps from a .nex file  
     
    [n, ts] = nex_ts(filename, varname)  
     
    INPUT:  
      filename - if empty string, will use File Open dialog  
      varname - variable name  
    OUTPUT:  
      n - number of timestamps  
      ts - array of timestamps (in seconds)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_ts.m)
  """

  return Runtime.call("nex_ts", *args, **kwargs)
