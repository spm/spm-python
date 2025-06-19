from spm._runtime import Runtime


def _db_close(*args, **kwargs):
    """
      DB_CLOSE closes the connection to the database  
         
        Use as  
          db_close  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_close.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_close", *args, **kwargs, nargout=0)
