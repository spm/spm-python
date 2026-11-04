from spm._runtime import Runtime


def _fixvolume(*args, **kwargs):
    r"""
      FIXVOLUME cleans up the volume data representation, removes old and obsoleted  
        fields and ensures that it is consistent with the most recent code.  
         
        Use as  
          output = fixvolume(input)  
        where input is a structure representing volume data  
         
        See also FT_CHECKDATA, FIXSOURCE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/fixvolume.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixvolume", *args, **kwargs)
