from mpython import Runtime


def _surf_to_tetgen(*args, **kwargs):
    """
      This function converts a triangulated mesh in FieldTrip format into a
        surface structure readable by Tetgen software


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/surf_to_tetgen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("surf_to_tetgen", *args, **kwargs, nargout=0)
