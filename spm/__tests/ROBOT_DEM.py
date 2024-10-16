from spm.__wrapper__ import Runtime


def ROBOT_DEM(*args, **kwargs):
  """  Tests routines in DEM GUI  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/ROBOT_DEM.m)
  """

  return Runtime.call("ROBOT_DEM", *args, **kwargs)
