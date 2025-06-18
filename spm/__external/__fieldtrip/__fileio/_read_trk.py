from mpython import Runtime


def _read_trk(*args, **kwargs):
    """
     read TrackVis .trk format data
        fillPath: filename of track to read.
       for format details http://www.trackvis.org/docs/?subsect=fileformat


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_trk.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_trk", *args, **kwargs)
