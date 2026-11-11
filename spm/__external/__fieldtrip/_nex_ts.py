from spm._runtime import Runtime


def _nex_ts(*args, **kwargs):
    r"""
      nex_ts(filename, varname): Read timestamps from a .nex file  
         
        [n, ts] = nex_ts(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
        OUTPUT:  
          n - number of timestamps  
          ts - array of timestamps (in seconds)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/nex_ts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nex_ts", *args, **kwargs)
