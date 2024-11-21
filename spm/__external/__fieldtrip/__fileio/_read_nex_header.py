from spm.__wrapper__ import Runtime


def _read_nex_header(*args, **kwargs):
    """
      READ_NEX_HEADER for Plexon *.nex file  
         
        Use as  
          [hdr] = read_nex_header(filename)  
         
        See also RAD_NEX_DATA, READ_NEX_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nex_header", *args, **kwargs)
