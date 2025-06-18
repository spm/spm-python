from mpython import Runtime


def _getdimord(*args, **kwargs):
    """
      GETDIMORD determine the dimensions and order of a data field in a FieldTrip
        structure.

        Use as
          dimord = getdimord(data, field)

        See also GETDIMSIZ, GETDATFIELD, FIXDIMORD


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/getdimord.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getdimord", *args, **kwargs)
