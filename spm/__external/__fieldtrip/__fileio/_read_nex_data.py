from spm.__wrapper__ import Runtime


def _read_nex_data(*args, **kwargs):
    """
      READ_NEX_DATA for Plexon *.nex file  
         
        Use as  
          [dat] = read_nex_data(filename, hdr, begsample, endsample, chanindx)  
         
        See also READ_NEX_HEADER, READ_NEX_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nex_data", *args, **kwargs)
