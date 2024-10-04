from spm.__wrap__ import _Runtime


def getCTFdata(*args, **kwargs):
  """   getCTFdata.m   Reads specified trials from .meg4 files in CTF-format data set.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/ctf/getCTFdata.m)
  """

  return _Runtime.call("getCTFdata", *args, **kwargs)
