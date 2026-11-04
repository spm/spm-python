from spm._runtime import Runtime


def _db_insert_blob(*args, **kwargs):
    r"""
      DB_INSERT_BLOB converts a Matlab variable of arbitrary type into  
        a binary stream and inserts this stream into a binary blob in the  
        database table.  
         
        Use as  
          db_insert_blob(tablename, fieldname, s)  
         
        See also DB_OPEN, DB_SELECT, DB_SELECT_BLOB, DB_INSERT, DB_CLOSE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/db_insert_blob.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_insert_blob", *args, **kwargs, nargout=0)
