from spm.__wrap__ import _Runtime


def _swapmemfile(*args, **kwargs):
  """  SWAPMEMFILE swaps a variable from file into memory and clears it   
    again from the memory on the subsequent call  
     
    Use with extreme caution!  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/swapmemfile.m)
  """

  return _Runtime.call("swapmemfile", *args, **kwargs)
