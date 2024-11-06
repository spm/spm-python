from spm.__wrapper__ import Runtime


def _nex_marker(*args, **kwargs):
    """
      nex_marker(filename, varname): Read a marker variable from a .nex file  
         
        [n, nm, nl, ts, names, m] = nex_marker(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
         
                  continuous (a/d) data come in fragments. Each fragment has a timestamp  
                  and a number of a/d data points. The timestamp corresponds to  
                  the time of recording of the first a/d value in this fragment.  
                  All the data values stored in the vector d.   
        OUTPUT:  
          n - number of markers  
          nm - number of fields in each marker  
          nl - number of characters in each marker field  
          ts - array of marker timestamps (in seconds)  
          names - names of marker fields ([nm 64] character array)  
          m - character array of marker values [n nl nm]  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_marker.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nex_marker", *args, **kwargs)
