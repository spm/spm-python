from spm.__wrap__ import _Runtime


def spm_MDP_plot(*args, **kwargs):
  """  creates a movie of hierarchical expectations and outcomes  
    FORMAT spm_MDP_plot(MDP))  
     
    MDP - nested MDP (and DEM) structures  
        - (requires fields to specify the labels of states and outcomes)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_plot.m)
  """

  return _Runtime.call("spm_MDP_plot", *args, **kwargs, nargout=0)
