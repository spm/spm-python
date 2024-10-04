from spm.__wrap__ import _Runtime


def bf_write_spmeeg(*args, **kwargs):
  """  Writes out beamformer results as M/EEG dataset  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_spmeeg.m)
  """

  return _Runtime.call("bf_write_spmeeg", *args, **kwargs)
