from spm.__wrap__ import _Runtime


def _det2x2(*args, **kwargs):
  """  DET2X2 computes determinant of matrix x, using explicit analytic definition  
    if size(x,1) < 4, otherwise use MATLAB det-function  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/det2x2.m)
  """

  return _Runtime.call("det2x2", *args, **kwargs)
