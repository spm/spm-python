from mpython import Runtime


def ft_struct2string(*args, **kwargs):
    """
      FT_STRUCT2STRING converts all char-array elements in a structure
        into strings.

        Use as
          x = ft_struct2string(x)

        See also FT_STRUCT2CHAR, FT_STRUCT2SINGLE, FT_STRUCT2DOUBLE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_struct2string.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_struct2string", *args, **kwargs)
