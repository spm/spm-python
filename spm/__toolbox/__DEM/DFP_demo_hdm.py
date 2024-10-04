from spm.__wrap__ import _Runtime


def DFP_demo_hdm(*args, **kwargs):
  """  demo for Hemodynamic deconvolution usinf variational filtering  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DFP_demo_hdm.m)
  """

  return _Runtime.call("DFP_demo_hdm", *args, **kwargs, nargout=0)
