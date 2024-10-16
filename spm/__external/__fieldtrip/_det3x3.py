from spm.__wrapper__ import Runtime


def _det3x3(*args, **kwargs):
  """  DET3X3 computes determinant of matrix x, using explicit analytic definition  
    if size(x) = [3 3 K M]  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/det3x3.m)
  """

  return Runtime.call("det3x3", *args, **kwargs)
