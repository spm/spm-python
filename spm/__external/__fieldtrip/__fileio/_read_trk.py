from spm._runtime import Runtime


def _read_trk(*args, **kwargs):
    r"""
     read TrackVis .trk format data  
        fillPath: filename of track to read.  
       for format details http://www.trackvis.org/docs/?subsect=fileformat  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_trk.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_trk", *args, **kwargs)
