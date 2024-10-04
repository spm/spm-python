from spm.__wrap__ import _Runtime


def bf_save_path(*args, **kwargs):
  """  Saves BF data in a MAT file  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_save_path.m)
  """

  return _Runtime.call("bf_save_path", *args, **kwargs, nargout=0)
