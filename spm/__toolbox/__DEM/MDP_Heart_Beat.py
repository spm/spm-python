from spm.__wrap__ import _Runtime


def MDP_Heart_Beat(*args, **kwargs):
  """  This simulation uses a Markov Decision process formulation of active  
    inference to demonstrate the interaction between interoceptive and  
    exteroceptive perception. This relies upon the fact that the function of  
    exteroceptive sense organs depends upon oscillatory cycles in  
    interoceptive states. The example used here is the change in retinal  
    blood flow, and its influence on vision, during a cardiac cycle.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/MDP_Heart_Beat.m)
  """

  return _Runtime.call("MDP_Heart_Beat", *args, **kwargs)
