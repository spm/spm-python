from spm.__wrap__ import _Runtime


def ADEM_lorenz_entropy(*args, **kwargs):
  """  This demo shows how structure can be instilled from an environment. It  
    uses an agent that optimises its recognition density over successive  
    epochs of exposure to an environment. This environment causes the agent  
    to flow on a Lorenz attractor with random perturbations. As the agent  
    learns the causal regularities in its environment, it is better able to  
    predict them and act to oppose the random effect. The result is that it  
    is more robust to random forces and therefore exhibits states with lower  
    entropy. This routine takes several minutes to run.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_lorenz_entropy.m)
  """

  return _Runtime.call("ADEM_lorenz_entropy", *args, **kwargs, nargout=0)
