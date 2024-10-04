from spm.__wrap__ import _Runtime


def _neuralynx_timestamp(*args, **kwargs):
  """ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
    SUBFUNCTION for reading a single timestamp of a single channel Neuralynx file  
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/neuralynx_timestamp.m)
  """

  return _Runtime.call("neuralynx_timestamp", *args, **kwargs)
