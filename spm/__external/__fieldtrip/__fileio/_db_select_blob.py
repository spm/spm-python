from spm.__wrap__ import _Runtime


def _db_select_blob(*args, **kwargs):
  """  DB_SELECT_BLOB selects a binary blob from a database table and converts  
    it back into a Matlab variable. The variable can be of an arbitrary type.  
     
    Use as  
      s = db_select_blob(tablename, fieldname)  
      s = db_select_blob(tablename, fieldname, num)  
     
    The optional argument num allows you to select a specific row number.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_select_blob.m)
  """

  return _Runtime.call("db_select_blob", *args, **kwargs)
