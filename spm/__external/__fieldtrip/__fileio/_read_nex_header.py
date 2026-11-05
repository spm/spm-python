from spm._runtime import Runtime


def _read_nex_header(*args, **kwargs):
    r"""
      READ_NEX_HEADER for Plexon *.nex file  
         
        Use as  
          [hdr] = read_nex_header(filename)  
         
        See also RAD_NEX_DATA, READ_NEX_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nex_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nex_header", *args, **kwargs)
