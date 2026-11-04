from spm._runtime import Runtime


def _read_wdq_header(*args, **kwargs):
    r"""
      READ_WDQ_HEADER reads header information from wdq files  
         
        Use as  
         [hdr] = read_wdq_header(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_wdq_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_wdq_header", *args, **kwargs)
