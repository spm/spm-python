from spm.__wrapper__ import Runtime


def _nex_ts(*args, **kwargs):
    """
      nex_ts(filename, varname): Read timestamps from a .nex file  
         
        [n, ts] = nex_ts(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
        OUTPUT:  
          n - number of timestamps  
          ts - array of timestamps (in seconds)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_ts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nex_ts", *args, **kwargs)
