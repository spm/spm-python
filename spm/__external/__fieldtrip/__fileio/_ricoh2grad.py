from spm.__wrap__ import _Runtime


def _ricoh2grad(*args, **kwargs):
  """  RICOH2GRAD converts the position and weights of all coils that  
    compromise a gradiometer system into a structure that can be used  
    by FieldTrip. This implementation uses the "ricoh_meg_reader" toolbox.  
     
    See also FT_READ_HEADER, CTF2GRAD, BTI2GRAD, FIF2GRAD, YOKOGAWA2GRAD_NEW  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ricoh2grad.m)
  """

  return _Runtime.call("ricoh2grad", *args, **kwargs)
