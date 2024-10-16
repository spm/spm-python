from spm.__wrapper__ import Runtime


def _fixdipole(*args, **kwargs):
  """  FIXDIPOLE ensures that the dipole position and moment are  
    consistently represented throughout FieldTrip functions.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixdipole.m)
  """

  return Runtime.call("fixdipole", *args, **kwargs)
