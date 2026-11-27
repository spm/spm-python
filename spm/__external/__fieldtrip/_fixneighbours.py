from spm._runtime import Runtime


def _fixneighbours(*args, **kwargs):
    r"""
      This function converts the old format of the neighbourstructure into the  
        new format - although it just works as a wrapper  
         
        See also FT_NEIGHBOURSELECTION  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fixneighbours.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixneighbours", *args, **kwargs)
