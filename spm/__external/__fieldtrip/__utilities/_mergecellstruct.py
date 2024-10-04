from spm.__wrap__ import _Runtime


def _mergecellstruct(*args, **kwargs):
  """  MERGECELLSTRUCT is a helper function for FT_TEST  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mergecellstruct.m)
  """

  return _Runtime.call("mergecellstruct", *args, **kwargs)
