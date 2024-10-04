from spm.__wrap__ import _Runtime


def _timestamp_neuralynx(*args, **kwargs):
  """  TIMESTAMP_NEURALYNX merge the low and high part of Neuralynx timestamps  
    into a single uint64 value  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/timestamp_neuralynx.m)
  """

  return _Runtime.call("timestamp_neuralynx", *args, **kwargs)
