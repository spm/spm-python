from spm.__wrapper__ import Runtime


def DFP_demo_hdm(*args, **kwargs):
  """  demo for Hemodynamic deconvolution usinf variational filtering  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DFP_demo_hdm.m)
  """

  return Runtime.call("DFP_demo_hdm", *args, **kwargs, nargout=0)
