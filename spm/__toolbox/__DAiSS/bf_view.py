from spm.__wrapper__ import Runtime


def bf_view(*args, **kwargs):
  """  Display the results of beamforming analysis  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view.m)
  """

  return Runtime.call("bf_view", *args, **kwargs)
