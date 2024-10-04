from spm.__wrap__ import _Runtime


def _neuralynx_crc(*args, **kwargs):
  """  NEURALYNX_CRC computes a cyclic redundancy check  
     
    Use as  
      crc = neuralynx_crc(dat)  
     
    Note that the CRC is computed along the first dimension.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/neuralynx_crc.m)
  """

  return _Runtime.call("neuralynx_crc", *args, **kwargs)
