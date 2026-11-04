from spm._runtime import Runtime


def _filetype_check_extension(*args, **kwargs):
    r"""
      FILETYPE_CHECK_EXTENSION helper function to determine the file type  
        by performing a case insensitive string comparison of the extension.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/filetype_check_extension.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("filetype_check_extension", *args, **kwargs)
