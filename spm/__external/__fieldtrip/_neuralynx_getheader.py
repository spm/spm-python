from mpython import Runtime


def _neuralynx_getheader(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        SUBFUNCTION for reading the 16384 byte header from any Neuralynx file
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/neuralynx_getheader.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("neuralynx_getheader", *args, **kwargs)
