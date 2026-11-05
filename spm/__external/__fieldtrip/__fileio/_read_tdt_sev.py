from spm._runtime import Runtime


def _read_tdt_sev(*args, **kwargs):
    r"""
      READ_TDT_SEV  
         
        Use as  
          sev = read_tdt_sev(filename, dtype, begsample, endsample)  
         
        Note: sev files contain raw broadband data that is streamed to the RS4  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tdt_sev.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_sev", *args, **kwargs)
