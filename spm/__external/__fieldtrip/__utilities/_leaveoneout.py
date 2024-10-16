from spm.__wrapper__ import Runtime


def _leaveoneout(*args, **kwargs):
  """leaveoneout is a function.  
      data = leaveoneout(data)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/leaveoneout.m)
  """

  return Runtime.call("leaveoneout", *args, **kwargs)
