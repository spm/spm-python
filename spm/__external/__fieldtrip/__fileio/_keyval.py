from mpython import Runtime


def _keyval(*args, **kwargs):
    """
      KEYVAL returns the value that corresponds to the requested key in a
        key-value pair list of variable input arguments

        Use as
          [val] = keyval(key, varargin)

        See also VARARGIN


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/keyval.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keyval", *args, **kwargs)
