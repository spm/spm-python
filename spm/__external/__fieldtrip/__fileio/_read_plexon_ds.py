from spm.__wrapper__ import Runtime


def _read_plexon_ds(*args, **kwargs):
    """
      READ_PLEXON_DS reads multiple single-channel Plexon files that are  
        all contained in a single directory. Each file is treated as a single  
        channel of a combined multi-channel dataset.  
         
        Use as  
          hdr = read_plexon_ds(dirname)  
          dat = read_plexon_ds(dirname,  hdr, begsample, endsample, chanindx)  
         
        See also READ_PLEXON_NEX, READ_PLEXON_PLX, READ_PLEXON_DDT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_plexon_ds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_plexon_ds", *args, **kwargs)
