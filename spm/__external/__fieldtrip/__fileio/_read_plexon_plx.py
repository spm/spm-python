from spm.__wrapper__ import Runtime


def _read_plexon_plx(*args, **kwargs):
    """
      READ_PLEXON_PLX reads header or data from a Plexon *.plx file, which  
        is a file containing action-potential (spike) timestamps and waveforms  
        (spike channels), event timestamps (event channels), and continuous  
        variable data (continuous A/D channels).  
         
        Use as  
          [hdr] = read_plexon_plx(filename)  
          [dat] = read_plexon_plx(filename, ...)  
          [dat1, dat2, dat3, hdr] = read_plexon_plx(filename, ...)  
         
        Optional input arguments should be specified in key-value pairs  
          'header'           = structure with header information  
          'memmap'           = 0 or 1  
          'feedback'         = 0 or 1  
          'ChannelIndex'     = number, or list of numbers (that will result in multiple outputs)  
          'SlowChannelIndex' = number, or list of numbers (that will result in multiple outputs)  
          'EventIndex'       = number, or list of numbers (that will result in multiple outputs)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_plexon_plx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_plexon_plx", *args, **kwargs)
