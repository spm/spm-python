from mpython import Runtime


def _loadama(*args, **kwargs):
    """
      LOADAMA read an inverted A-matrix and associated geometry information
        from an ama file that was written by Tom Oostendorp's DIPOLI

        Use as
          [ama] = loadama(filename)

        See also LOADTRI, LOADMAT


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/loadama.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadama", *args, **kwargs)
