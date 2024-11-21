from spm.__wrapper__ import Runtime


def _convert_segmentationstyle(*args, **kwargs):
    """
      CONVERT_SEGMENTATIONSTYLE is a helper function for converting between probabilistic  
        and indexed representations. It is used by FT_DATATYPE_SEGMENTATION and  
        FT_DATATYPE_PARCELLATION.  
         
        See also FIXSEGMENTATION, DETERMINE_SEGMENTATIONSTYLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/convert_segmentationstyle.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("convert_segmentationstyle", *args, **kwargs)
