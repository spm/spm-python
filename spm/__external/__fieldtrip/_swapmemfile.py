from spm.__wrapper__ import Runtime


def _swapmemfile(*args, **kwargs):
  """  SWAPMEMFILE swaps a variable from file into memory and clears it   
    again from the memory on the subsequent call  
     
    Use with extreme caution!  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/swapmemfile.m)
  """

  return Runtime.call("swapmemfile", *args, **kwargs)
