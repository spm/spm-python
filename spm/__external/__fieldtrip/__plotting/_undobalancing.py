from spm.__wrapper__ import Runtime


def _undobalancing(*args, **kwargs):
  """  UNDOBALANCING removes all balancing coefficients from the gradiometer sensor array  
     
    This is used in CHANNELPOSITION, FT_PREPARE_LAYOUT, FT_SENSTYPE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/undobalancing.m)
  """

  return Runtime.call("undobalancing", *args, **kwargs)
