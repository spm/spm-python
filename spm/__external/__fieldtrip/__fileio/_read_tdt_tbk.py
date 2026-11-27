from spm._runtime import Runtime


def _read_tdt_tbk(*args, **kwargs):
    r"""
      tbk file has block events information and time marks  
        for efficiently locate event if query by time  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tdt_tbk.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tbk", *args, **kwargs)
