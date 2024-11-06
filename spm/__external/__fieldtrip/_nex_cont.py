from spm.__wrapper__ import Runtime


def _nex_cont(*args, **kwargs):
    """
      nex_cont(filename, varname): Read continuous variable from a .nex file  
         
        [adfreq, n, ts, fn, d] = nex_cont(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
         
                  continuous (a/d) data come in fragments. Each fragment has a timestamp  
                  and a number of a/d data points. The timestamp corresponds to  
                  the time of recording of the first a/d value in this fragment.  
                  All the data values stored in the vector d.   
        OUTPUT:  
          n - total number of data points   
          ts - array of fragment timestamps (one timestamp for fragment, in seconds)  
          fn - number of data points in each fragment  
          d - array of a/d values (in millivolts)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_cont.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nex_cont", *args, **kwargs)
