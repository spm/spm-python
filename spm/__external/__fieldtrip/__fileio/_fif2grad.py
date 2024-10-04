from spm.__wrap__ import _Runtime


def _fif2grad(*args, **kwargs):
  """  FIF2GRAD constructs a gradiometer definition from a Neuromag *.fif file  
    The resulting gradiometer definition can be used by Fieldtrip for forward  
    and inverse computations.  
     
    Use as  
    grad = fif2grad(filename)  
     
    See also CTF2GRAD, BTI2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,  
    FT_READ_SENS, FT_READ_HEADER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fif2grad.m)
  """

  return _Runtime.call("fif2grad", *args, **kwargs)
