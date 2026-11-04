from spm._runtime import Runtime


def _read_besa_swf(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_besa_swf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_besa_swf", *args, **kwargs)
