from spm.__wrapper__ import Runtime


def _decode_res4(*args, **kwargs):
  """  DECODE_RES4 is a helper function for real-time processing of CTF data. This  
    function is used to decode the content of the optional ctf_res4 chunck.  
     
    See also DECODE_FIF, DECODE_NIFTI1, SAP2MATLAB  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/decode_res4.m)
  """

  return Runtime.call("decode_res4", *args, **kwargs)
