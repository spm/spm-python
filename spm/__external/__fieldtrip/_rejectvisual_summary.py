from spm.__wrapper__ import Runtime


def _rejectvisual_summary(*args, **kwargs):
  """  SUBFUNCTION for ft_rejectvisual  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/rejectvisual_summary.m)
  """

  return Runtime.call("rejectvisual_summary", *args, **kwargs)
