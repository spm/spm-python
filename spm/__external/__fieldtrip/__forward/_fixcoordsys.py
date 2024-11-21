from spm.__wrapper__ import Runtime


def _fixcoordsys(*args, **kwargs):
    """
      FIXCOORDSYS ensures that the coordinate system is consistently  
        described. E.g. SPM and MNI are technically the same coordinate  
        system, but the strings 'spm' and 'mni' are different.  
         
        See also FT_DETERMINE_COORDSYS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/fixcoordsys.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixcoordsys", *args, **kwargs)
