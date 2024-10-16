from spm.__wrapper__ import Runtime


def _ft_fetch_data(*args, **kwargs):
  """  FT_FETCH_DATA mimics the behavior of FT_READ_DATA, but for a FieldTrip  
    raw data structure instead of a file on disk.  
     
    Use as  
      [dat] = ft_fetch_data(data, ...)  
     
    See also FT_READ_DATA, FT_FETCH_HEADER, FT_FETCH_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_fetch_data.m)
  """

  return Runtime.call("ft_fetch_data", *args, **kwargs)
