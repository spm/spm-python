from spm._runtime import Runtime


def _read_eyelink_asc(*args, **kwargs):
    r"""
      READ_EYELINK_ASC reads the header information, input triggers, messages  
        and optional data points from an Eyelink *.asc file. The output is either  
        a pair of FieldTrip compatible hdr and event structures, or a data structure  
        containing the low-level header information, and the requested data  
        matrix  
         
        Use as  
          [hdr, event] = read_eyelink_asc(filename)  
        or  
          [asc] = read_eyelink_asc(filename, hdr, begsample, endsample, chanindx)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_eyelink_asc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_eyelink_asc", *args, **kwargs)
