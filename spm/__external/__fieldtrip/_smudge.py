from spm.__wrap__ import _Runtime


def _smudge(*args, **kwargs):
  """  SMUDGE(DATIN, TRI) computes a smudged version of the input data datain,  
    given a triangulation tri. The algorithm is according to what is in  
    MNE-Suite, documented in chapter 8.3  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/smudge.m)
  """

  return _Runtime.call("smudge", *args, **kwargs)
