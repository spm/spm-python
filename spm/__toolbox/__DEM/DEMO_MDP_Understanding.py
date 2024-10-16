from spm.__wrapper__ import Runtime


def DEMO_MDP_Understanding(*args, **kwargs):
  """  This demo uses a hierarchical version of the ubiquitous T-maze demo, in  
    which the agent is equipped with a space of hypotheses about why it chose  
    to act in a certain way. This means that, when queried, it is able to  
    communicate an explanation for its actions.  
     
    see also: DEM_demo_MDP_X.m and spm_MPD_VB_X.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_MDP_Understanding.m)
  """

  return Runtime.call("DEMO_MDP_Understanding", *args, **kwargs)
