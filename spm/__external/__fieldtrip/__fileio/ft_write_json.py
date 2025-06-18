from mpython import Runtime


def ft_write_json(*args, **kwargs):
    """
      FT_WRITE_JSON writes a MATLAB structure to a JSON file. Compared to the builtin
        MATLAB function, this implementation deals a bit different with missing values,
        booleans, and NaNs, and results in a more human-readable file.

        Use as
          ft_write_json(filename, struct)

        See also FT_READ_JSON, JSONDECODE, JSONENCODE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_json.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_write_json", *args, **kwargs, nargout=0)
