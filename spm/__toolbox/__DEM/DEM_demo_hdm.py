from spm.__wrap__ import _Runtime


def DEM_demo_hdm(*args, **kwargs):
  """  demo for Hemodynamic deconvolution  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_hdm.m)
  """

  return _Runtime.call("DEM_demo_hdm", *args, **kwargs, nargout=0)
