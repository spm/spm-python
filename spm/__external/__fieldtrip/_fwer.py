from spm.__wrap__ import _Runtime


def _fwer(*args, **kwargs):
  """  FWER family-wise error rate control using Bonferoni method  
     
    Use as  
      h = fwer(p, q)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/fwer.m)
  """

  return _Runtime.call("fwer", *args, **kwargs)
