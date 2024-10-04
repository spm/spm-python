from spm.__wrap__ import _Runtime


def _fixdipole(*args, **kwargs):
  """  FIXDIPOLE ensures that the dipole position and moment are  
    consistently represented throughout FieldTrip functions.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/fixdipole.m)
  """

  return _Runtime.call("fixdipole", *args, **kwargs)
