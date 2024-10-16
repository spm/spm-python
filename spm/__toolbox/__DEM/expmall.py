from spm.__wrapper__ import Runtime


def expmall(*args, **kwargs):
  """expmall is a function.  
      dx = expmall(J, f, t, EP)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/expmall.m)
  """

  return Runtime.call("expmall", *args, **kwargs)
