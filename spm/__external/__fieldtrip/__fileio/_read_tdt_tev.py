from spm._runtime import Runtime


def _read_tdt_tev(*args, **kwargs):
    r"""
      READ_TDT_TANK  
         
        Use as  
          [tev, tsq] = read_tdt_tank(filename)  
         
        Note:  
          tev file contains event binary data  
          tev and tsq files work together to get an event's data and attributes  
          sev files contains streamed binary data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tdt_tev.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tev", *args, **kwargs)
