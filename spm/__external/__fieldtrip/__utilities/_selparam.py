from spm.__wrap__ import _Runtime


def _selparam(*args, **kwargs):
  """  SELPARAM(DATA) extracts the fieldnames param of the structure data containing functional  
    data, which have a dimensionality consistent with the dimord field in the data. Selparam  
    is a helper function to selectdata  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/selparam.m)
  """

  return _Runtime.call("selparam", *args, **kwargs)
