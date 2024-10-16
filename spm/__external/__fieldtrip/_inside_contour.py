from spm.__wrapper__ import Runtime


def _inside_contour(*args, **kwargs):
  """inside_contour is a function.  
      bool = inside_contour(pos, contour)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/inside_contour.m)
  """

  return Runtime.call("inside_contour", *args, **kwargs)
