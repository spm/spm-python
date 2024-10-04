from spm.__wrap__ import _Runtime


def DEM_demo_double_well(*args, **kwargs):
  """  DEMO comparing DEM with particle filtering in the context of a bimodal  
    conditional density.  This demonstrates a shortcoming of DEM in that it  
    fails to represent the true density.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_double_well.m)
  """

  return _Runtime.call("DEM_demo_double_well", *args, **kwargs, nargout=0)
