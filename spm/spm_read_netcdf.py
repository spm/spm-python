from spm._runtime import Runtime


def spm_read_netcdf(*args, **kwargs):
    r"""
      Read the header information from a NetCDF file into a data structure  
        FORMAT cdf = spm_read_netcdf(fname)  
        fname - name of NetCDF file  
        cdf   - data structure  
         
        See: http://www.unidata.ucar.edu/packages/netcdf/  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_read_netcdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_read_netcdf", *args, **kwargs)
