from spm.__wrapper__ import Runtime


def _defaultId(*args, **kwargs):
  """  DEFAULTID returns a string that can serve as warning or error identifier,  
    for example 'FieldTip:ft_read_header:line345'.  
     
    See also WARNING, ERROR, FT_NOTICE, FT_INFO, FT_DEBUG  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/private/defaultId.m)
  """

  return Runtime.call("defaultId", *args, **kwargs)
