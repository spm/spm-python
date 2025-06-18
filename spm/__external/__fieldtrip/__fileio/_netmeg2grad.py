from mpython import Runtime


def _netmeg2grad(*args, **kwargs):
    """
      NETMEG2GRAD converts a NetMEG header to a gradiometer structure
        that can be understood by FieldTrip and Robert Oostenveld's low-level
        forward and inverse routines. This function only works for headers
        that have been read using FT_READ_DATA and NETCDF.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/netmeg2grad.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("netmeg2grad", *args, **kwargs)
