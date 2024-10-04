from spm.__wrap__ import _Runtime


def ADEM_lorenz(*args, **kwargs):
  """  Action-DEM demo specifying an attractor (in terms of the parameters of  
    desired equations of motion) This demo first exposes an agent to a Lorenz  
    attractor world such that it can learn the three parameters of the Lorenz  
    system. It is then placed in a test world with a fixed point attractor to  
    see if it has remembered the chaotic dynamics it learnt in the training  
    environment  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_lorenz.m)
  """

  return _Runtime.call("ADEM_lorenz", *args, **kwargs, nargout=0)
