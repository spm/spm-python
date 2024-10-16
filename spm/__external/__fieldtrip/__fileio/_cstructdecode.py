from spm.__wrapper__ import Runtime


def _cstructdecode(*args, **kwargs):
  """  CSTRUCTDECODE decodes a structure from a uint8 buffer  
     
    See READ_NEURALYNX_NEV for an example  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/cstructdecode.m)
  """

  return Runtime.call("cstructdecode", *args, **kwargs)
