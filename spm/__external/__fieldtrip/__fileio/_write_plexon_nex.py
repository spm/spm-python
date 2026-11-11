from spm._runtime import Runtime


def _write_plexon_nex(*args, **kwargs):
    r"""
      WRITE_PLEXON_NEX writes a Plexon *.nex file, which is a file  
        containing action-potential (spike) timestamps and waveforms (spike  
        channels), event timestamps (event channels), and continuous variable  
        data (continuous A/D channels).  
         
        Use as  
          write_plexon_nex(filename, nex);  
         
        The data structure should contain  
          nex.hdr.FileHeader.Frequency  = TimeStampFreq  
          nex.hdr.VarHeader.Type       = type, 5 for continuous  
          nex.hdr.VarHeader.Name       = label, padded to length 64  
          nex.hdr.VarHeader.WFrequency = sampling rate of continuous channel  
          nex.var.dat                  = data  
          nex.var.ts                   = timestamps  
         
        See also READ_PLEXON_NEX, READ_PLEXON_PLX, READ_PLEXON_DDT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_plexon_nex.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_plexon_nex", *args, **kwargs, nargout=0)
