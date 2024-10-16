from spm.__wrapper__ import Runtime


def _netmeg2grad(*args, **kwargs):
  """  NETMEG2GRAD converts a NetMEG header to a gradiometer structure  
    that can be understood by FieldTrip and Robert Oostenveld's low-level  
    forward and inverse routines. This function only works for headers  
    that have been read using FT_READ_DATA and NETCDF.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/netmeg2grad.m)
  """

  return Runtime.call("netmeg2grad", *args, **kwargs)
