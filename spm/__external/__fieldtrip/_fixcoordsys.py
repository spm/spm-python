from spm._runtime import Runtime


def _fixcoordsys(*args, **kwargs):
    r"""
      FIXCOORDSYS ensures that the coordinate system is consistently  
        described. E.g. SPM and MNI are technically the same coordinate  
        system, but the strings 'spm' and 'mni' are different.  
         
        See also FT_DETERMINE_COORDSYS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fixcoordsys.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixcoordsys", *args, **kwargs)
