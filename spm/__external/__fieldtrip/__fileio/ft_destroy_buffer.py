from spm.__wrap__ import _Runtime


def ft_destroy_buffer(*args, **kwargs):
  """  FT_DESTROY_BUFFER stops the thread with the TCP server attached to  
    the local MATLAB instance and removes all data from memory.  
     
    Use as  
      ft_destroy_buffer  
     
    See also FT_CREATE_BUFFER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_destroy_buffer.m)
  """

  return _Runtime.call("ft_destroy_buffer", *args, **kwargs, nargout=0)
