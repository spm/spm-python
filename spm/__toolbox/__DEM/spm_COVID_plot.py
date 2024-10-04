from spm.__wrap__ import _Runtime


def spm_COVID_plot(*args, **kwargs):
  """  Graphics for coronavirus simulations  
    FORMAT spm_COVID_plot(Y,X,Z)  
    Y      - expected timeseries (i.e., new depths and cases)  
    X      - latent (marginal ensemble density) states  
    Z      - optional empirical data  
    u      - optional bed capacity threshold  
    U      - optional indices of outcomes  
     
    This auxiliary routine plots the trajectory of outcome variables  
    and underlying latent or hidden states, in the form of marginal densities  
    over the four factors that constitute the COVID model. if empirical data  
    are supplied, they will be superimposed.  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_plot.m)
  """

  return _Runtime.call("spm_COVID_plot", *args, **kwargs, nargout=0)
