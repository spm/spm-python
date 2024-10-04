from spm.__wrap__ import _Runtime


def _leaveoneout(*args, **kwargs):
  """leaveoneout is a function.  
      data = leaveoneout(data)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/leaveoneout.m)
  """

  return _Runtime.call("leaveoneout", *args, **kwargs)
