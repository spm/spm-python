from spm.__wrapper__ import Runtime


def _channelconnectivity(*args, **kwargs):
  """  CHANNELCONNECTIVIY creates a NxN matrix that describes whether channels  
    are connected as neighbours  
     
    See also FT_PREPARE_NEIGHBOURS, TRIANGLE2CONNECTIVITY  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/channelconnectivity.m)
  """

  return Runtime.call("channelconnectivity", *args, **kwargs)
