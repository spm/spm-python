from spm.__wrapper__ import Runtime


def _filetype_check_header(*args, **kwargs):
    """
      FILETYPE_CHECK_HEADER helper function to determine the file type  
        by reading the first number of bytes of a file and comparing them  
        to a known string or magic number.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/filetype_check_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("filetype_check_header", *args, **kwargs)
