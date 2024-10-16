from spm.__wrapper__ import Runtime


def bf_view_glass(*args, **kwargs):
  """  Diplays glass brain plot of DAISS output results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view_glass.m)
  """

  return Runtime.call("bf_view_glass", *args, **kwargs)
