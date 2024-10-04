from spm.__wrap__ import _Runtime


def _yokogawa2grad(*args, **kwargs):
  """  YOKOGAWA2GRAD converts the position and weights of all coils that  
    compromise a gradiometer system into a structure that can be used  
    by FieldTrip. This implementation uses the old "yokogawa" toolbox.  
     
    See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD,  
    FT_READ_SENS, FT_READ_HEADER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/yokogawa2grad.m)
  """

  return _Runtime.call("yokogawa2grad", *args, **kwargs)
