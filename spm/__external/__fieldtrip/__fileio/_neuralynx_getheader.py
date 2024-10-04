from spm.__wrap__ import _Runtime


def _neuralynx_getheader(*args, **kwargs):
  """ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
    SUBFUNCTION for reading the 16384 byte header from any Neuralynx file  
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/neuralynx_getheader.m)
  """

  return _Runtime.call("neuralynx_getheader", *args, **kwargs)
