from mpython import Runtime


def ft_transform_vol(*args, **kwargs):
    """
      This function is a backward compatibility wrapper for existing MATLAB scripts
        that call a function that is not part of the FieldTrip toolbox any more.

        Please update your code to make it future-proof.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_transform_vol.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_transform_vol", *args, **kwargs)
