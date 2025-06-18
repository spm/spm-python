from mpython import Runtime


def _db_select_blob(*args, **kwargs):
    """
      DB_SELECT_BLOB selects a binary blob from a database table and converts
        it back into a Matlab variable. The variable can be of an arbitrary type.

        Use as
          s = db_select_blob(tablename, fieldname)
          s = db_select_blob(tablename, fieldname, num)

        The optional argument num allows you to select a specific row number.

        See also DB_OPEN, DB_INSERT, DB_SELECT, DB_INSERT_BLOB, DB_CLOSE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/db_select_blob.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("db_select_blob", *args, **kwargs)
