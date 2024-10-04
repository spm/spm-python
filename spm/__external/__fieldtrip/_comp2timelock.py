from spm.__wrap__ import _Runtime


def _comp2timelock(*args, **kwargs):
  """  COMP2TIMELOCK transform the independent components into something  
    on which the timelocked source reconstruction methods can  
    perform their trick.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/comp2timelock.m)
  """

  return _Runtime.call("comp2timelock", *args, **kwargs)
