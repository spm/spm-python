from spm.__wrap__ import _Runtime


def _guidelines(*args, **kwargs):
  """  GUIDELINES searches for a contiguous block of commented text and shows  
    its contents. It is used to display additional help sections.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/guidelines.m)
  """

  return _Runtime.call("guidelines", *args, **kwargs)
