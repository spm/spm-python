from spm.__wrapper__ import Runtime


def ft_poll_buffer(*args, **kwargs):
  """  FT_POLL_BUFFER is deprecated.  
     
    Please use FT_READ_DATA and FT_READ_EVENT with the  'blocking' and  
    the 'timeout' options.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_poll_buffer.m)
  """

  return Runtime.call("ft_poll_buffer", *args, **kwargs)
