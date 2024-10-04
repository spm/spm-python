from spm.__wrap__ import _Runtime


def spm_MDP_G(*args, **kwargs):
  """  auxiliary function for Bayesian suprise or mutual information  
    FORMAT [G] = spm_MDP_G(A,x)  
     
    A   - likelihood array (probability of outcomes given causes)  
    x   - probability density of causes  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_G.m)
  """

  return _Runtime.call("spm_MDP_G", *args, **kwargs)
