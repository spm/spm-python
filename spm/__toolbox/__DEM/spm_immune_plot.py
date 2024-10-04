from spm.__wrap__ import _Runtime


def spm_immune_plot(*args, **kwargs):
  """  Plotting for immune model  
    FORMAT y = spm_immune_plot(P,c,M,U)  
    P - Priors  
    c - covariance  
    U - inputs (timing of measurements)  
    Y - data  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_plot.m)
  """

  return _Runtime.call("spm_immune_plot", *args, **kwargs)
