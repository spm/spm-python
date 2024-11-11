from spm.__wrapper__ import Runtime


def _determine_segmentationstyle(*args, **kwargs):
    """
      DETERMINE_SEGMENTATIONSTYLE is a helper function that determines the type of segmentation  
        contained in each of the fields. It is used by FT_DATATYPE_SEGMENTATION and  
        FT_DATATYPE_PARCELLATION.  
         
        See also FIXSEGMENTATION, CONVERT_SEGMENTATIONSTYLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/determine_segmentationstyle.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("determine_segmentationstyle", *args, **kwargs)
