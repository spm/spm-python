from spm.__wrap__ import _Runtime


def _rv(*args, **kwargs):
  """  RV returns the relative residual variance between measured and simulated data  
     
    rv = rv(measured, simulated)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/rv.m)
  """

  return _Runtime.call("rv", *args, **kwargs)
