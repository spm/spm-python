from spm.__wrapper__ import Runtime


def _isdir_or_mkdir(*args, **kwargs):
    """
      ISDIR_OR_MKDIR Checks that a directory exists, or if not, creates the directory and  
        all its parent directories.  
         
        See also FOPEN_OR_ERROR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/isdir_or_mkdir.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isdir_or_mkdir", *args, **kwargs, nargout=0)
