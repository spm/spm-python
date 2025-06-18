from mpython import Runtime


def _db_select(*args, **kwargs):
    """
      DB_SELECT selects data from a database table and converts it into a
        Matlab structure.Each of the fields in the database table will be
        represented as field in the strucure.

        Use as
          s = db_select(tablename, fields)
          s = db_select(tablename, fields, num)

        The optional argument num allows you to select a specific row number.

        See also DB_OPEN, DB_INSERT, DB_SELECT_BLOB, DB_INSERT_BLOB, DB_CLOSE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_select.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_select", *args, **kwargs)
