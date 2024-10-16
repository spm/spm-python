from spm.__wrapper__ import Runtime


def _join_str(*args, **kwargs):
  """join_str is a function.  
      t = join_str(separator, cells)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/join_str.m)
  """

  return Runtime.call("join_str", *args, **kwargs)
