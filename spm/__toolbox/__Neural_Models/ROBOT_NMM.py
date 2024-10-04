from spm.__wrap__ import _Runtime


def ROBOT_NMM(*args, **kwargs):
  """  Tests routines in neural mass model (NMM) GUI  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/ROBOT_NMM.m)
  """

  return _Runtime.call("ROBOT_NMM", *args, **kwargs)
