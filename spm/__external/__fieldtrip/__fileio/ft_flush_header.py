from spm.__wrap__ import _Runtime


def ft_flush_header(*args, **kwargs):
  """  FT_FLUSH_HEADER removes the header information from the data queue  
    this also removes all data associated with the specific header.  
     
    Use as  
      ft_flush_header(filename, ...)  
     
    See also FT_FLUSH_DATA, FT_FLUSH_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_header.m)
  """

  return _Runtime.call("ft_flush_header", *args, **kwargs, nargout=0)
