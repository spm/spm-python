from spm.__wrapper__ import Runtime


def _read_plexon_nex(*args, **kwargs):
    """
      READ_PLEXON_NEX reads header or data from a Plexon *.nex file, which  
        is a file containing action-potential (spike) timestamps and waveforms  
        (spike channels), event timestamps (event channels), and continuous  
        variable data (continuous A/D channels).  
         
        LFP and spike waveform data that is returned by this function is   
        expressed in microVolt.  
         
        Use as  
          [hdr] = read_plexon_nex(filename)  
          [dat] = read_plexon_nex(filename, ...)  
          [dat1, dat2, dat3, hdr] = read_plexon_nex(filename, ...)  
         
        Optional arguments should be specified in key-value pairs and can be  
          header      structure with header information  
          feedback    0 or 1  
          tsonly      0 or 1, read only the timestamps and not the waveforms  
          channel     number, or list of numbers (that will result in multiple outputs)  
          begsample   number (for continuous only)  
          endsample   number (for continuous only)  
         
        See also READ_PLEXON_PLX, READ_PLEXON_DDT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_plexon_nex.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_plexon_nex", *args, **kwargs)
