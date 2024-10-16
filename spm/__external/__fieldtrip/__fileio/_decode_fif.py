from spm.__wrapper__ import Runtime


def _decode_fif(*args, **kwargs):
  """  DECODE_FIF is a helper function for real-time processing of Neuromag data. This  
    function is used to decode the content of the optional neuromag_fif chunk(s).  
     
    See also DECODE_RES4, DECODE_NIFTI1, SAP2MATLAB  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/decode_fif.m)
  """

  return Runtime.call("decode_fif", *args, **kwargs)
