from spm._runtime import Runtime


def _isplottingfunction(*args, **kwargs):
    r"""
      ISPLOTTINGFUNCTION is a helper function for reproducescript, and  
        is used for the cfg.reproducescript functionality. It compares the input  
        function name with the list of known FieldTrip plotting functions and  
        returns 1 if it is a plotting function, and 0 otherwise.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/isplottingfunction.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isplottingfunction", *args, **kwargs)
