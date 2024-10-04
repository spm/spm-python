from spm.__wrap__ import _Runtime


def ADEM_mountaincar_loss(*args, **kwargs):
  """  This demo re-visits the mountain car problem to show that adaptive  
    (desired) behaviour can be prescribed in terms of loss-functions (i.e.  
    reward functions of state-space).  
    It exploits the fact that under the free-energy formulation, loss is  
    divergence. This means that priors can be used to make certain parts of  
    state-space costly (i.e. with high divergence) and others rewarding (low  
    divergence). Active inference under these priors will lead to sampling of  
    low cost states and (apparent) attractiveness of those states.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_mountaincar_loss.m)
  """

  return _Runtime.call("ADEM_mountaincar_loss", *args, **kwargs, nargout=0)
