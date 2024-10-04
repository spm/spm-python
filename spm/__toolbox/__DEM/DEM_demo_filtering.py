from spm.__wrap__ import _Runtime


def DEM_demo_filtering(*args, **kwargs):
  """  State-space demo routine comparing Bayesian filtering and DEM:  The  
    system here is chosen to highlight changes in conditional moments  
    (including precision) induced by nonlinearities in the model.  A  
    comparative evaluation is provided using extended Kalman filtering and  
    particle filtering. Crucially, DEM and particle filtering deal gracefully  
    with nonlinearities, in relation to Kalman filtering.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_filtering.m)
  """

  return _Runtime.call("DEM_demo_filtering", *args, **kwargs, nargout=0)
