from spm.__wrapper__ import Runtime


def _fopen_or_error(*args, **kwargs):
    """
      FOPEN_OR_ERROR Opens a file, like fopen, but throws an exception if the open failed.  
         
        This keeps you from having to write "if fid < 0; error(...)" everywhere  
        you do an fopen.  
         
        See also FOPEN, ISDIR_OR_MKDIR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fopen_or_error.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fopen_or_error", *args, **kwargs)
