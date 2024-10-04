from spm.__wrap__ import _Runtime


def expmall(*args, **kwargs):
  """expmall is a function.  
      dx = expmall(J, f, t, EP)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/expmall.m)
  """

  return _Runtime.call("expmall", *args, **kwargs)
