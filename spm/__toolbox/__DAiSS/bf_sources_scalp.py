from spm.__wrapper__ import Runtime


def bf_sources_scalp(*args, **kwargs):
  """  Generate source space on the scalp surface, as a part of measuring a  
    magnetomyogram (MMG) of the face.  
      
    See https://doi.org/10.1111/psyp.13507 for more information.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources_scalp.m)
  """

  return Runtime.call("bf_sources_scalp", *args, **kwargs)
