from spm.__wrapper__ import Runtime


def DEMO_AI_NLSI(*args, **kwargs):
  """  Demo of active inference for trust games  
   __________________________________________________________________________  
     
    This routine uses a Markov decision process formulation of active  
     
    see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_AI_NLSI.m)
  """

  return Runtime.call("DEMO_AI_NLSI", *args, **kwargs)
