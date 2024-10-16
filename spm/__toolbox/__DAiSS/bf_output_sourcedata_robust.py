from spm.__wrapper__ import Runtime


def bf_output_sourcedata_robust(*args, **kwargs):
  """  Extract source data, handling bad data segments  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_sourcedata_robust.m)
  """

  return Runtime.call("bf_output_sourcedata_robust", *args, **kwargs)
