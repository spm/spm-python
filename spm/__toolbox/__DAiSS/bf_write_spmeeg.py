from spm.__wrapper__ import Runtime


def bf_write_spmeeg(*args, **kwargs):
  """  Writes out beamformer results as M/EEG dataset  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_spmeeg.m)
  """

  return Runtime.call("bf_write_spmeeg", *args, **kwargs)
