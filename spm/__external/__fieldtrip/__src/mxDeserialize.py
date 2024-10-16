from spm.__wrapper__ import Runtime


def mxDeserialize(*args, **kwargs):
  """  MXDESERIALIZE reconstructs a MATLAB object from a uint8 array suitable  
    for passing down a comms channel to be reconstructed at the other end.  
     
    See also MXSERIALIZE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/mxDeserialize.m)
  """

  return Runtime.call("mxDeserialize", *args, **kwargs)
