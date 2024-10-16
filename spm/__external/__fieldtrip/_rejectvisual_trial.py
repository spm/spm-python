from spm.__wrapper__ import Runtime


def _rejectvisual_trial(*args, **kwargs):
  """  SUBFUNCTION for ft_rejectvisual  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/rejectvisual_trial.m)
  """

  return Runtime.call("rejectvisual_trial", *args, **kwargs)
