from spm.__wrap__ import _Runtime


def DEM_demo_Lagrangian(*args, **kwargs):
  """  Demo to illustrate divergence and curl free flow specified by a   
    Lagrangian and antisymmetric matrices. This example uses a double well   
    potential and Newtonian dynamics.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Lagrangian.m)
  """

  return _Runtime.call("DEM_demo_Lagrangian", *args, **kwargs, nargout=0)
