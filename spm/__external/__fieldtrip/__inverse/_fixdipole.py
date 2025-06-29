from spm._runtime import Runtime


def _fixdipole(*args, **kwargs):
    """
      FIXDIPOLE ensures that the dipole position and moment are  
        consistently represented throughout FieldTrip functions.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/fixdipole.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixdipole", *args, **kwargs)
