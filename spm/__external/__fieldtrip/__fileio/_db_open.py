from spm.__wrapper__ import Runtime


def _db_open(*args, **kwargs):
    """
      DB_OPEN opens the connection to the database  
         
        Use as  
           db_open  
           db_open(user, password, server, port, database)  
           db_open('mysql://<user>:<password>@<host>:<port>')  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_open.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("db_open", *args, **kwargs, nargout=0)
