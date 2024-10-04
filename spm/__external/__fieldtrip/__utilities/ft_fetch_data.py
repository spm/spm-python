from spm.__wrap__ import _Runtime


def ft_fetch_data(*args, **kwargs):
  """  FT_FETCH_DATA mimics the behavior of FT_READ_DATA, but for a FieldTrip  
    raw data structure instead of a file on disk.  
     
    Use as  
      [dat] = ft_fetch_data(data, ...)  
     
    See also FT_READ_DATA, FT_FETCH_HEADER, FT_FETCH_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_fetch_data.m)
  """

  return _Runtime.call("ft_fetch_data", *args, **kwargs)
