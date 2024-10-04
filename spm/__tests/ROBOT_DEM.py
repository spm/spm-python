from spm.__wrap__ import _Runtime


def ROBOT_DEM(*args, **kwargs):
  """  Tests routines in DEM GUI  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/ROBOT_DEM.m)
  """

  return _Runtime.call("ROBOT_DEM", *args, **kwargs)
