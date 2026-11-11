from spm._runtime import Runtime


def _fixdipole(*args, **kwargs):
    r"""
      FIXDIPOLE ensures that the dipole position and moment are  
        consistently represented throughout FieldTrip functions.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fixdipole.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixdipole", *args, **kwargs)
