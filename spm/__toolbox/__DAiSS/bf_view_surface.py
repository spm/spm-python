from spm.__wrap__ import _Runtime


def bf_view_surface(*args, **kwargs):
  """  Diplay surface plot of DAISS output results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view_surface.m)
  """

  return _Runtime.call("bf_view_surface", *args, **kwargs)
