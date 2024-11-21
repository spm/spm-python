from spm.__wrapper__ import Runtime


def _db_insert(*args, **kwargs):
    """
      DB_INSERT inserts a structure into a database table. Each field of  
        the structure should correspond with one of the fields in the table.  
         
        Use as  
          db_insert(tablename, s)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_insert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("db_insert", *args, **kwargs, nargout=0)
