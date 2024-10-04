from spm.__wrap__ import _Runtime


def _inv2x2(*args, **kwargs):
  """  INV2X2 computes inverse of matrix x, using explicit analytic definition  
    if size(x,1) < 4, otherwise use MATLAB inv-function  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/inv2x2.m)
  """

  return _Runtime.call("inv2x2", *args, **kwargs)
