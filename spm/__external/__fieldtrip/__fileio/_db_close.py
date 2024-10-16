from spm.__wrapper__ import Runtime


def _db_close(*args, **kwargs):
  """  DB_CLOSE closes the connection to the database  
     
    Use as  
      db_close  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_close.m)
  """

  return Runtime.call("db_close", *args, **kwargs, nargout=0)
