from spm.__wrap__ import _Runtime


def _encode_nifti1(*args, **kwargs):
  """ function blob = encode_nifti1(H)  
     
    Encodes a NIFTI-1 header (=> raw 348 bytes (uint8)) from a Matlab structure  
    that matches the C struct defined in nifti1.h.  
     
    WARNING: This function currently ignores endianness !!!  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/encode_nifti1.m)
  """

  return _Runtime.call("encode_nifti1", *args, **kwargs)
