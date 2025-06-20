from spm._runtime import Runtime


def _filetype_check_extension(*args, **kwargs):
    """
      FILETYPE_CHECK_EXTENSION helper function to determine the file type  
        by performing a case insensitive string comparison of the extension.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/filetype_check_extension.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("filetype_check_extension", *args, **kwargs)
