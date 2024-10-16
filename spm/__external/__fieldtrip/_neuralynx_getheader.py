from spm.__wrapper__ import Runtime


def _neuralynx_getheader(*args, **kwargs):
  """ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
    SUBFUNCTION for reading the 16384 byte header from any Neuralynx file  
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/neuralynx_getheader.m)
  """

  return Runtime.call("neuralynx_getheader", *args, **kwargs)
