from spm.__wrap__ import _Runtime


def _print_tim(*args, **kwargs):
  """  SUBFUNCTION for pretty-printing time in hours, minutes, ...  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/print_tim.m)
  """

  return _Runtime.call("print_tim", *args, **kwargs)
