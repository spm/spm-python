from spm.__wrap__ import _Runtime


def _rejectvisual_summary(*args, **kwargs):
  """  SUBFUNCTION for ft_rejectvisual  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/rejectvisual_summary.m)
  """

  return _Runtime.call("rejectvisual_summary", *args, **kwargs)
