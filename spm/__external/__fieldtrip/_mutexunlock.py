from mpython import Runtime


def _mutexunlock(*args, **kwargs):
    """
      MUTEXUNLOCK removes a lockfile

        Use as
          mutexunlock(lockfile)

        See also MUTEXLOCK and http://en.wikipedia.org/wiki/Mutual_exclusion


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mutexunlock.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mutexunlock", *args, **kwargs, nargout=0)
