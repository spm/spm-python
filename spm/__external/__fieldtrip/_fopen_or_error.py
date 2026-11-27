from spm._runtime import Runtime


def _fopen_or_error(*args, **kwargs):
    r"""
      FOPEN_OR_ERROR Opens a file, like fopen, but throws an exception if the open failed.  
         
        This keeps you from having to write "if fid < 0; error(...)" everywhere  
        you do an fopen.  
         
        See also FOPEN, ISDIR_OR_MKDIR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fopen_or_error.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fopen_or_error", *args, **kwargs)
