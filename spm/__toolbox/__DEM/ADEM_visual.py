from spm.__wrap__ import _Runtime


def ADEM_visual(*args, **kwargs):
  """  DEM demo for active inference (i.e. action-perception optimisation of free  
    energy).  This simulation calls on spm_ADEM to simulate visual sampling of  
    the world and demonstrate retinal stabilisation or visual tracking. We  
    simulate a simple 2-D plaid stimulus and subject it to an exogenous  
    perturbations. By employing tight and broad priors on the location of the  
    stimulus, we can show that action does and does not explain away the visual  
    consequences of the perturbation (i.e., the movement is seen or not).  This  
    illustrates how one can reframe stabilisation or tracking in terms of  
    sampling sensory input to ensure conditional expectations are met; and  
    how these expectations are shaped by prior expectations.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_visual.m)
  """

  return _Runtime.call("ADEM_visual", *args, **kwargs, nargout=0)
