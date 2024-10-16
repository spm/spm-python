from spm.__wrapper__ import Runtime


def _ft_struct2json(*args, **kwargs):
  """   FT_STRUCT2JSON  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_struct2json.m)
  """

  return Runtime.call("ft_struct2json", *args, **kwargs)
