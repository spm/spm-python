from spm._runtime import Runtime


def _filetype_check_header(*args, **kwargs):
    r"""
      FILETYPE_CHECK_HEADER helper function to determine the file type  
        by reading the first number of bytes of a file and comparing them  
        to a known string or magic number.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/filetype_check_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("filetype_check_header", *args, **kwargs)
