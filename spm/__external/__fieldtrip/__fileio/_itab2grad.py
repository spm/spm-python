from spm.__wrapper__ import Runtime


def _itab2grad(*args, **kwargs):
  """  ITAB2GRAD converts the original Chieti ITAB header structure into  
    a gradiometer definition that is compatible with FieldTrip forward  
    and inverse computations  
     
    See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, YOKOGAWA2GRAD,  
    FT_READ_SENS, FT_READ_HEADER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/itab2grad.m)
  """

  return Runtime.call("itab2grad", *args, **kwargs)
