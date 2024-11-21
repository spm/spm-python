from spm.__wrapper__ import Runtime


def _read_besa_swf(*args, **kwargs):
    """
      READ_BESA_SWF  
         
        Use as  
          [swf] = read_besa_swf(filename)  
         
        This will return a structure with the header information in  
          swf.label     cell-array with labels  
          swf.data      data matrix, Nchan X Npnts  
          swf.npnt  
          swf.tsb  
          swf.di  
          swf.sb  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_swf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_besa_swf", *args, **kwargs)
