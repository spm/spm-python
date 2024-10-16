from spm.__wrapper__ import Runtime


def bf_write(*args, **kwargs):
  """  Write out the results of beamforming analysis  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write.m)
  """

  return Runtime.call("bf_write", *args, **kwargs)
