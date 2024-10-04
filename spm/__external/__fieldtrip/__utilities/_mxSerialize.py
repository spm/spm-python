from spm.__wrap__ import _Runtime


def _mxSerialize(*args, **kwargs):
  """  MXSERIALIZE converts any MATLAB object into a uint8 array suitable  
    for passing down a comms channel to be reconstructed at the other end.  
     
    See also MXDESERIALIZE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mxSerialize.m)
  """

  return _Runtime.call("mxSerialize", *args, **kwargs)
