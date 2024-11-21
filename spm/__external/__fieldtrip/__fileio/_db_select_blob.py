from spm.__wrapper__ import Runtime


def _db_select_blob(*args, **kwargs):
    """
      DB_SELECT_BLOB selects a binary blob from a database table and converts  
        it back into a Matlab variable. The variable can be of an arbitrary type.  
         
        Use as  
          s = db_select_blob(tablename, fieldname)  
          s = db_select_blob(tablename, fieldname, num)  
         
        The optional argument num allows you to select a specific row number.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_select_blob.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("db_select_blob", *args, **kwargs)
