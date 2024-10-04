from spm.__wrap__ import _Runtime


def bf_save(*args, **kwargs):
  """  Save BF data in a MAT file  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_save.m)
  """

  return _Runtime.call("bf_save", *args, **kwargs, nargout=0)
