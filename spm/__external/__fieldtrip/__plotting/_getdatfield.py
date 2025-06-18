from mpython import Runtime


def _getdatfield(*args, **kwargs):
    """
      GETDATFIELD

        Use as
          [datfield, dimord] = getdatfield(data)
        where the output arguments are cell-arrays.

        See also GETDIMORD, GETDIMSIZ


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/getdatfield.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getdatfield", *args, **kwargs)
