from spm.__wrap__ import _Runtime


def spm_mar_prior(*args, **kwargs):
  """  Specify ARD-type prior for Bayesian MAR model  
    function [prior] = spm_mar_prior (d,p,type)  
     
    d         Number of time series  
    p         Order of MAR model  
    type      'global', 'lag','interaction','lag-inter',  
              'silly','ran2','triu' (see code below)  
     
    prior     data structure to be passed to spm_mar.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar_prior.m)
  """

  return _Runtime.call("spm_mar_prior", *args, **kwargs)
