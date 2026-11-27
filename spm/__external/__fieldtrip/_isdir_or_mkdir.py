from spm._runtime import Runtime


def _isdir_or_mkdir(*args, **kwargs):
    r"""
      ISDIR_OR_MKDIR Checks that a directory exists, or if not, creates the directory and  
        all its parent directories.  
         
        See also FOPEN_OR_ERROR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/isdir_or_mkdir.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isdir_or_mkdir", *args, **kwargs, nargout=0)
