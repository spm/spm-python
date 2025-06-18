from mpython import Runtime


def _neuralynx_timestamp(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        SUBFUNCTION for reading a single timestamp of a single channel Neuralynx file
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/neuralynx_timestamp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("neuralynx_timestamp", *args, **kwargs)
