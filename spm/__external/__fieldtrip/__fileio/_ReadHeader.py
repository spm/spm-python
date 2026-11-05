from spm._runtime import Runtime


def _ReadHeader(*args, **kwargs):
    r"""
      H = ReadHeader(fp)  
         
         Reads NSMA header, leaves file-read-location at end of header  
         
         INPUT:  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ReadHeader.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ReadHeader", *args, **kwargs)
