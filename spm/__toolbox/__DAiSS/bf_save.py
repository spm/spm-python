from spm.__wrapper__ import Runtime


def bf_save(*args, **kwargs):
  """  Save BF data in a MAT file  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_save.m)
  """

  return Runtime.call("bf_save", *args, **kwargs, nargout=0)
