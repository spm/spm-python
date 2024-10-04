from spm.__wrap__ import _Runtime


def _transfer2coeffs(*args, **kwargs):
  """  TRANSFER2COEFFS converts a spectral transfer matrix into the time domain  
    equivalent multivariate autoregressive coefficients up to a specified  
    lag, starting from lag 1.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/transfer2coeffs.m)
  """

  return _Runtime.call("transfer2coeffs", *args, **kwargs)
