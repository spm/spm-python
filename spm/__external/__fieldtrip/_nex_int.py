from spm.__wrapper__ import Runtime


def _nex_int(*args, **kwargs):
    """
      nex_int(filename, varname): Read interval variable from a .nex file  
         
        [n, ts_left, ts_right] = nex_int(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
        OUTPUT:  
          n - number of intervals  
          ts_left - array of left ends of the intervals (in seconds)  
          ts_right - array of right ends of the intervals (in seconds)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_int.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nex_int", *args, **kwargs)
