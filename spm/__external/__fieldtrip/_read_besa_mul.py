from spm.__wrap__ import _Runtime


def _read_besa_mul(*args, **kwargs):
  """  READ_BESA_MUL reads data from a BESA multiplexed (*.mul) file  
     
    Use as  
      dat = read_besa_mul(filename);  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_mul.m)
  """

  return _Runtime.call("read_besa_mul", *args, **kwargs)
