from spm.__wrapper__ import Runtime


def spm_read_netcdf(*args, **kwargs):
  """  Read the header information from a NetCDF file into a data structure  
    FORMAT cdf = spm_read_netcdf(fname)  
    fname - name of NetCDF file  
    cdf   - data structure  
     
    See: http://www.unidata.ucar.edu/packages/netcdf/  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_read_netcdf.m)
  """

  return Runtime.call("spm_read_netcdf", *args, **kwargs)
