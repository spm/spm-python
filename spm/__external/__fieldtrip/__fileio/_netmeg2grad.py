from spm._runtime import Runtime


def _netmeg2grad(*args, **kwargs):
    r"""
      NETMEG2GRAD converts a NetMEG header to a gradiometer structure  
        that can be understood by FieldTrip and Robert Oostenveld's low-level  
        forward and inverse routines. This function only works for headers  
        that have been read using FT_READ_DATA and NETCDF.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/netmeg2grad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("netmeg2grad", *args, **kwargs)
