from spm._runtime import Runtime


def _convert_segmentationstyle(*args, **kwargs):
    r"""
      CONVERT_SEGMENTATIONSTYLE is a helper function for converting between probabilistic  
        and indexed representations. It is used by FT_DATATYPE_SEGMENTATION and  
        FT_DATATYPE_PARCELLATION.  
         
        See also FIXSEGMENTATION, DETERMINE_SEGMENTATIONSTYLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/convert_segmentationstyle.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("convert_segmentationstyle", *args, **kwargs)
