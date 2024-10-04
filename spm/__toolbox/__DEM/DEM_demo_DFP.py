from spm.__wrap__ import _Runtime


def DEM_demo_DFP(*args, **kwargs):
  """  DEM demo for linear deconvolution:  This demo considers the deconvolution  
    of the responses of a single-input-multiple output input-state-output  
    model (DCM) to disclose the input or causes.  It starts by demonstrating  
    Variational filtering with spm_DFP; this is a stochastic filtering scheme  
    that propagates particles over a changing variational energy landscape   
    such that their sample density can be used to approximate the underlying  
    ensemble or conditional density.  We then repeat the inversion using   
    spm_DEM (i.e., under a Laplace assumption) which involves integrating the  
    path of just one particle (i.e., the mode).  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_DFP.m)
  """

  return _Runtime.call("DEM_demo_DFP", *args, **kwargs, nargout=0)
