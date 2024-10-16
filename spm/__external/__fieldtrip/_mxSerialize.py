from spm.__wrapper__ import Runtime


def _mxSerialize(*args, **kwargs):
  """  MXSERIALIZE converts any MATLAB object into a uint8 array suitable  
    for passing down a comms channel to be reconstructed at the other end.  
     
    See also MXDESERIALIZE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mxSerialize.m)
  """

  return Runtime.call("mxSerialize", *args, **kwargs)
