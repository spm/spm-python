from spm.__wrapper__ import Runtime


def DEM_demo_OU(*args, **kwargs):
  """  DEM demo for linear deconvolution:  This demo considers the deconvolution  
    of one of the simplest dynamical process; a random walk or Ornstein-  
    Uhlenbeck process.  It shows how DEM can infer on the causes as stochastic  
    innovations (c.f., Bayesian filtering) by exploiting temporal  
    correlations.  Strictly speaking this is not a Ornstein-Uhlenbeck process  
    because the innovations are themselves correlated and would normally be a  
    Wiener process  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_OU.m)
  """

  return Runtime.call("DEM_demo_OU", *args, **kwargs, nargout=0)
