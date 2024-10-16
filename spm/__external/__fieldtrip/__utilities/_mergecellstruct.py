from spm.__wrapper__ import Runtime


def _mergecellstruct(*args, **kwargs):
  """  MERGECELLSTRUCT is a helper function for FT_TEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mergecellstruct.m)
  """

  return Runtime.call("mergecellstruct", *args, **kwargs)
