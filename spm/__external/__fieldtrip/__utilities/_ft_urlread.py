from spm.__wrapper__ import Runtime


def _ft_urlread(*args, **kwargs):
  """  FT_URLREAD  
     
    The documentation of R2016b states that urlread is not recommended.  
    Use webread or webwrite instead.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_urlread.m)
  """

  return Runtime.call("ft_urlread", *args, **kwargs)
