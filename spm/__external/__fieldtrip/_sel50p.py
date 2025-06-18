from mpython import Runtime


def _sel50p(*args, **kwargs):
    """
      This function will add the field "subspace" to the grid definition.

        The subspace projection corresponds to selecting 50% of the
        channels that are the closest to the dipole.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/sel50p.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sel50p", *args, **kwargs)
