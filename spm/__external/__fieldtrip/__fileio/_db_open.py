from spm.__wrapper__ import Runtime


def _db_open(*args, **kwargs):
  """  DB_OPEN opens the connection to the database  
     
    Use as  
       db_open  
       db_open(user, password, server, port, database)  
       db_open('mysql://<user>:<password>@<host>:<port>')  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_open.m)
  """

  return Runtime.call("db_open", *args, **kwargs, nargout=0)
