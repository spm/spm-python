from mpython import Runtime


def _isrealvec(*args, **kwargs):
    """
      ISREALVEC returns true for a real row or column vector

        Use as
          status = isrealvec(x)

        See also ISNUMERIC, ISREAL, ISVECTOR, ISREALMAT


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/isrealvec.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isrealvec", *args, **kwargs)
