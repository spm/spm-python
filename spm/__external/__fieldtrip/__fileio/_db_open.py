from mpython import Runtime


def _db_open(*args, **kwargs):
    """
      DB_OPEN opens the connection to the database

        Use as
           db_open
           db_open(user, password, server, port, database)
           db_open('mysql://<user>:<password>@<host>:<port>')

        See also DB_CLOSE, DB_SELECT, DB_INSERT, DB_SELECT_BLOB, DB_INSERT_BLOB


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_open.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_open", *args, **kwargs, nargout=0)
