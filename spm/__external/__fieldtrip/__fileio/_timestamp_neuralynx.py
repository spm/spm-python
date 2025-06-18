from mpython import Runtime


def _timestamp_neuralynx(*args, **kwargs):
    """
      TIMESTAMP_NEURALYNX merge the low and high part of Neuralynx timestamps
        into a single uint64 value


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/timestamp_neuralynx.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("timestamp_neuralynx", *args, **kwargs)
