from spm.__wrapper__ import Runtime


def _read_trk(*args, **kwargs):
    """
     read TrackVis .trk format data  
        fillPath: filename of track to read.  
       for format details http://www.trackvis.org/docs/?subsect=fileformat  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_trk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_trk", *args, **kwargs)
