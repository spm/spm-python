from spm.__wrapper__ import Runtime


def bf_output(*args, **kwargs):
  """  Perform postprocessing based on beamforming projectors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output.m)
  """

  return Runtime.call("bf_output", *args, **kwargs)
