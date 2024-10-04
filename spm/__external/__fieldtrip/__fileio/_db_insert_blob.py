from spm.__wrap__ import _Runtime


def _db_insert_blob(*args, **kwargs):
  """  DB_INSERT_BLOB converts a Matlab variable of arbitrary type into  
    a binary stream and inserts this stream into a binary blob in the  
    database table.  
     
    Use as  
      db_insert_blob(tablename, fieldname, s)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_insert_blob.m)
  """

  return _Runtime.call("db_insert_blob", *args, **kwargs, nargout=0)
