from spm._runtime import Runtime


def _fixsegmentation(*args, **kwargs):
    r"""
      FIXSEGMENTATION is a helper function that ensures the segmentation to be internally  
        consistent. It is used by FT_DATATYPE_SEGMENTATION and FT_DATATYPE_PARCELLATION.  
         
        % See also CONVERT_SEGMENTATIONSTYLE, DETERMINE_SEGMENTATIONSTYLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/fixsegmentation.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixsegmentation", *args, **kwargs)
