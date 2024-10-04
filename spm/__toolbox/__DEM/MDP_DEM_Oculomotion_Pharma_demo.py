from spm.__wrap__ import _Runtime


def MDP_DEM_Oculomotion_Pharma_demo(*args, **kwargs):
  """  Demo of mixed models for oculmotor behaviour, with pharmacological  
    manipulations  
     
   __________________________________________________________________________  
     
    This demo ilustrates the use of mixed (continuous and discrete)  
    generative models in simulating oculomotion. An MDP model is used to  
    select locations in visual space, and a continuous model is used to  
    implement these decisions. See also DEM_demo_MDP_DEM.m,  
    MDP_DEM_Oculomotion_demo.m  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/MDP_DEM_Oculomotion_Pharma_demo.m)
  """

  return _Runtime.call("MDP_DEM_Oculomotion_Pharma_demo", *args, **kwargs)
