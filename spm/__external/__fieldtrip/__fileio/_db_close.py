from spm._runtime import Runtime


def _db_close(*args, **kwargs):
    r"""
      DB_CLOSE closes the connection to the database  
         
        Use as  
          db_close  
         
        See also DB_OPEN, DB_SELECT, DB_INSERT, DB_SELECT_BLOB, DB_INSERT_BLOB  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/db_close.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_close", *args, **kwargs, nargout=0)
