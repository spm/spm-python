from mpython import Runtime


def _isplottingfunction(*args, **kwargs):
    """
      ISPLOTTINGFUNCTION is a helper function for reproducescript, and
        is used for the cfg.reproducescript functionality. It compares the input
        function name with the list of known FieldTrip plotting functions and
        returns 1 if it is a plotting function, and 0 otherwise.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/isplottingfunction.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isplottingfunction", *args, **kwargs)
