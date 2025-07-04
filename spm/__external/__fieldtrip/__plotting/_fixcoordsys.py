from spm._runtime import Runtime


def _fixcoordsys(*args, **kwargs):
    """
      FIXCOORDSYS ensures that the coordinate system is consistently  
        described. E.g. SPM and MNI are technically the same coordinate  
        system, but the strings 'spm' and 'mni' are different.  
         
        See also FT_DETERMINE_COORDSYS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/fixcoordsys.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixcoordsys", *args, **kwargs)
