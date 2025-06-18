from mpython import Runtime


def spm_read_netcdf(*args, **kwargs):
    """
      Read the header information from a NetCDF file into a data structure
        FORMAT cdf = spm_read_netcdf(fname)
        fname - name of NetCDF file
        cdf   - data structure

        See: http://www.unidata.ucar.edu/packages/netcdf/
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_read_netcdf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_read_netcdf", *args, **kwargs)
