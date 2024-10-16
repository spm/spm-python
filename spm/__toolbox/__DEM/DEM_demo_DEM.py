from spm.__wrapper__ import Runtime


def DEM_demo_DEM(*args, **kwargs):
  """  Triple estimation of states, parameters and hyperparameters:  
    This demo focuses estimating both the states and parameters to furnish a  
    complete system identification, given only the form of the system and its  
    responses to unknown input (c.f., DEM_demo_EM, which uses known inputs)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_DEM.m)
  """

  return Runtime.call("DEM_demo_DEM", *args, **kwargs, nargout=0)
