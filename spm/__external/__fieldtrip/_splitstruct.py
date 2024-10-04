from spm.__wrap__ import _Runtime


def _splitstruct(*args, **kwargs):
  """  SPLITSTRUCT splits a structure into names and values  
     
    See also PRINTSTRUCT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/splitstruct.m)
  """

  return _Runtime.call("splitstruct", *args, **kwargs)
