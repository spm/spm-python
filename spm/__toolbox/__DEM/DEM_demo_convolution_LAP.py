from spm.__wrapper__ import Runtime


def DEM_demo_convolution_LAP(*args, **kwargs):
  """  Linear convolution revisited: A dual estimation problem  
   __________________________________________________________________________  
    This demonstration compares generalised filtering and a state-of-the-art   
    Bayesian smoother (SCKS) in the context of dual estimation. Note that the  
    parameter estimates are smaller then the true values for generalised   
    schemes (LAP and DEM). This is largely due to the shrinkage priors and   
    optimisation of model evidence (marginal likelihood), as opposed to the  
    likelihood optimised by the Square-root Cubature Kalman Smoother (SCKS).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_convolution_LAP.m)
  """

  return Runtime.call("DEM_demo_convolution_LAP", *args, **kwargs, nargout=0)
