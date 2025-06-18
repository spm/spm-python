from mpython import Runtime


def _makessense(*args, **kwargs):
    """
      MAKESSENSE determines whether a some specific fields in a FieldTrip data structure
        make sense.

        Use as
          status = makessense(data, field)

        See also GETDIMORD, GETDIMSIZ, GETDATFIELD


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/makessense.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("makessense", *args, **kwargs)
