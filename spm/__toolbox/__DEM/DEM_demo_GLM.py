from spm.__wrap__ import _Runtime


def DEM_demo_GLM(*args, **kwargs):
  """  Demo comparing DEM and ReML (restricted maximum likelihood) under a simple  
    general linear model (GLM).  Slight differences in the hyperpriors of both  
    schemes make this an interesting exercise.  Note that ReML uses a  
    covariance hyper-parameterisation; whereas DEM uses precision  
    hyperparameters.  This demo uses a non-hierarchical GLM and switches the  
    roles of parameters and causes to illustrate their equivalence under a   
    DEM inversion.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_GLM.m)
  """

  return _Runtime.call("DEM_demo_GLM", *args, **kwargs, nargout=0)
