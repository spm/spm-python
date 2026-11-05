from spm._runtime import Runtime


def _read_nex5_header(*args, **kwargs):
    r"""
      READ_NEX5_HEADER for Nex Technologies *.nex5 file  
         
        Use as  
          [hdr] = read_nex5_header(filename)  
         
        See also RAD_NEX5_DATA, READ_NEX5_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nex5_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nex5_header", *args, **kwargs)
