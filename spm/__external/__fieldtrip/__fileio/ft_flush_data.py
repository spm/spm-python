from spm.__wrap__ import _Runtime


def ft_flush_data(*args, **kwargs):
  """  FT_FLUSH_DATA removes all data from the data queue  
     
    Use as  
      ft_flush_data(filename, ...)  
     
    See also FT_FLUSH_HEADER, FT_FLUSH_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_data.m)
  """

  return _Runtime.call("ft_flush_data", *args, **kwargs, nargout=0)
