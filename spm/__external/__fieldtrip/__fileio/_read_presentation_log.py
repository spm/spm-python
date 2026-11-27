from spm._runtime import Runtime


def _read_presentation_log(*args, **kwargs):
    r"""
      READ_PRESENTATION_LOG reads a NBS Presentation scenario log file and  
        represents it as a FieldTrip event structure.  
         
        See also FT_READ_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_presentation_log.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_presentation_log", *args, **kwargs)
