from spm.__wrap__ import _Runtime


def _db_insert(*args, **kwargs):
  """  DB_INSERT inserts a structure into a database table. Each field of  
    the structure should correspond with one of the fields in the table.  
     
    Use as  
      db_insert(tablename, s)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_insert.m)
  """

  return _Runtime.call("db_insert", *args, **kwargs, nargout=0)
