from spm.__wrap__ import _Runtime


def _db_close(*args, **kwargs):
  """  DB_CLOSE closes the connection to the database  
     
    Use as  
      db_close  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_close.m)
  """

  return _Runtime.call("db_close", *args, **kwargs, nargout=0)
