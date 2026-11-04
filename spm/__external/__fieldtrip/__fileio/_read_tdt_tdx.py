from spm._runtime import Runtime


def _read_tdt_tdx(*args, **kwargs):
    r"""
      tdx file contains just information about epoc,  
        is generated after recording if necessary for fast retrieve epoc information  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tdt_tdx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tdt_tdx", *args, **kwargs)
