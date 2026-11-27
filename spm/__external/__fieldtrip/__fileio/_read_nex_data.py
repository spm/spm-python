from spm._runtime import Runtime


def _read_nex_data(*args, **kwargs):
    r"""
      READ_NEX_DATA for Plexon *.nex file  
         
        Use as  
          [dat] = read_nex_data(filename, hdr, begsample, endsample, chanindx)  
         
        See also READ_NEX_HEADER, READ_NEX_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nex_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nex_data", *args, **kwargs)
